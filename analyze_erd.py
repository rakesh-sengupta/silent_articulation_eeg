# Install dependencies (run once)
!pip install mne pandas matplotlib seaborn

import os, glob
import mne, numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns

# === Parameters ===
DATA_DIR = '/content/drive/MyDrive/Silent_Art/'  # folder with .mff files (Change as necessary)
CHAN_RANGE = list(range(16,33))                 # E16–E32
EXTRA_CHAN = ['E65']                            # plus E65
CHANNELS = [f'E{ch}' for ch in CHAN_RANGE] + EXTRA_CHAN

TMIN, TMAX   = -2.0, 2.0
BASELINE     = (-2.0, -1.0)   # for TFR baseline
ACTIVE_WIN   = (0.0, 1.0)     # for ERD measurement
FREQS        = np.arange(8,13)  # alpha band
N_CYCLES     = FREQS / 2.0

results = []

# === Loop over subjects ===
mff_files = glob.glob(os.path.join(DATA_DIR, '*.mff'))
print(f"Found {len(mff_files)} .mff files in {DATA_DIR}")

for mff_path in mff_files:
    subj = os.path.basename(mff_path).replace('.mff','')
    print(f"\n=== Processing {subj} ===")

    # 1. Load & filter
    raw = mne.io.read_raw_egi(mff_path, preload=True, verbose=False)
    raw.filter(0.1, 40., fir_design='firwin', verbose=False)
    raw.notch_filter(50., verbose=False)

    # 2. Events mapping
    events, annot_id = mne.events_from_annotations(raw, verbose=False)
    cond_map = {}
    for name, code in [('covert_word','CAW_'),
                       ('overt_word','OAW_'),
                       ('covert_nonce','CNW_'),
                       ('overt_nonce','ONW_')]:
        if code in annot_id:
            cond_map[name] = annot_id[code]
    print("  Conditions found:", cond_map)

    # 3. Epoch (no baseline here)
    epochs = mne.Epochs(raw, events, cond_map,
                        tmin=TMIN, tmax=TMAX,
                        baseline=None, preload=True,
                        reject_by_annotation=True, verbose=False)

    # 4. ICA cleanup
    ica = mne.preprocessing.ICA(n_components=20, random_state=0)
    ica.fit(epochs, verbose=False)
    ica.exclude = [0, 1]
    epochs_clean = ica.apply(epochs.copy(), verbose=False)

    # 5. Re-reference to average
    epochs_clean.set_eeg_reference('average', projection=False, verbose=False)

    # 6. Pick our channels
    present = [ch for ch in CHANNELS if ch in epochs_clean.ch_names]
    if len(present)==0:
        print("  No channels of interest found; skipping.")
        continue
    print("  Picking channels:", present)
    epochs_clean.pick(present)

    # 7. Compute Morlet TFR and baseline‐correct in % change
    power = epochs_clean.compute_tfr(
        method='morlet', freqs=FREQS, n_cycles=N_CYCLES,
        use_fft=True, return_itc=False, decim=3, n_jobs=1, verbose=False
    )
    power.apply_baseline(baseline=BASELINE, mode='percent', verbose=False)

    times = power.times
    bmask = (times >= BASELINE[0]) & (times < BASELINE[1])
    amask = (times >= ACTIVE_WIN[0]) & (times < ACTIVE_WIN[1])

    # 8. Compute single‐trial ERD% and failure rate per condition
    for cond in cond_map:
        data = power[cond].data  # shape (n_epochs, n_ch, n_freqs, n_times)
        erd_vals = []
        for e in range(data.shape[0]):
            trial = data[e]
            bp = trial[:,:,bmask].mean()
            ap = trial[:,:,amask].mean()
            erd = 100. * (ap - bp) / (bp if bp!=0 else np.nan)
            erd_vals.append(erd)
        erd_vals = np.array(erd_vals)
        pct_fail = 100. * np.sum(erd_vals >= 0) / len(erd_vals)
        print(f"  {cond}: {len(erd_vals)} trials, %fail={pct_fail:.1f}%")
        results.append({'Subject': subj,
                        'Condition': cond,
                        'PercentFail': pct_fail})

# === Aggregate results ===
df = pd.DataFrame(results)

# 9. Plot group summary
if not df.empty:
    plt.figure(figsize=(8,5))
    sns.barplot(x='Condition', y='PercentFail', data=df,
                ci='sd', palette='Set1')
    sns.swarmplot(x='Condition', y='PercentFail', data=df,
                  color='k', alpha=0.7)
    plt.ylabel('% Trials without Alpha Drop')
    plt.ylim(0,100)
    plt.title('Single-Trial ERD Detection Error by Condition')
    plt.tight_layout()
    plt.show()
else:
    print("\nNo data processed. Plotting skipped.")
