# silent_articulation_eeg
# EEG Data for Covert and Overt Articulation Study

This repository provides documentation for an **EEG experiment** investigating different forms of articulation.

The raw electroencephalography (EEG) data files for this study are stored in the linked Google Drive folder. These files are in the **`.mff` (MFF - Minitab File Format / EGI Raw Data)** format, which is the native output format for the EGI NetStation acquisition system. Each `.mff` file contains a single participant's raw, 64-channel EEG data, synchronized with the experimental events.

**Data Location:** [Google Drive Folder containing .mff files](https://drive.google.com/drive/folders/1-zSDoenDhY3gJoS528-oiWr2aU89x1B6?usp=drive_link)

***

# Methods

## Participants

For **Phase 1** and **Phase 2** of the study, we recruited a group of **7** and **6** (respectively) healthy, right-handed adults with no history of neurological or speech disorders. All participants provided informed consent prior to their participation.

---

## EEG Data Acquisition

EEG data was recorded using an **EGI NetStation system** with **64 channels**. Electrodes were placed according to the international **10-20 system**. Data was streamed and synchronized with experimental events via NetStation connection. Electrode impedance was maintained below **5 k$\Omega$**.

---

## Experimental Paradigm

The experiment utilizes five conditions, presented in a fully randomized order.

* **Covert Articulation of Words (CAW):** Participants silently articulate real words.
* **Overt Articulation of Words (OAW):** Participants articulate real words aloud.
* **Covert Articulation of Nonce Words (CANW):** Participants silently articulate pronounceable nonce words (pseudo-words).
* **Overt Articulation of Nonce Words (OANW):** Participants articulate pronounceable nonce words aloud.
* **No Articulation (NA):** A control condition where participants passively observe a fixation cross.

### Trial Structure

The trial structure follows a set sequence:

1.  **Fixation (1000 ms):** A fixation cross `+` is presented at the center of the screen.
2.  **Condition Cue (500 ms):** A symbolic icon is displayed to indicate the trial's condition (e.g., an icon for 'silent', 'speak', or 'observe').
3.  **Stimulus Presentation (1500 ms):** For articulation conditions, the word or nonce word is presented. For the control (**NA**) condition, a fixation cross `+` is shown.
4.  **Articulation Period (2000 ms):** A fixation cross `+` is displayed on screen while participants perform the cued task (covertly articulating, overtly articulating, or observing).
5.  **Rest Period (1500 ms):** A blank screen is presented to mark the end of the trial.



### Stimuli

Word stimuli consist of **10 one-syllable** and **10 two-syllable** high-frequency English words. Nonce word stimuli consist of **10 one-syllable** and **10 two-syllable** pronounceable pseudo-words, matched to the general phonological structure of the real words.

| Real 1-syll | FreqPM | Real 2-syll | FreqPM | Nonce 1-syll | Nonce 2-syll |
| :--- | :--- | :--- | :--- | :--- | :--- |
| cat | 121.93 | bottle | 11.17 | lat | lanner |
| dog | 122.68 | button | 9.38 | zog | vebbin |
| jump | 21.31 | chicken | 12.98 | drap | blicken |
| plan | 56.82 | ladder | 3.99 | blan | gaddor |
| spin | 6.74 | dinner | 17.06 | snib | fubber |
| flag | 18.24 | garden | 15.84 | flagh | gorden |
| track | 21.45 | pillow | 4.59 | trat | nillow |
| grin | 4.19 | window | 18.76 | brin | wendoe |
| slap | 3.84 | muffin | 1.61 | plap | moppin |
| twig | 1.47 | hammer | 6.31 | twibz | gobblet |
*FreqPM = Frequency per Million (SUBTLEX-US)*

---

### Experimental Design

The experiment used a fully randomized within-subjects design for both phases.

#### Phase 1:
* Each of the 20 real words is presented **1 time** for the **CAW** condition and **1 time** for the **OAW** condition.
* Each of the 20 nonce words is presented **1 time** for the **CANW** condition and **1 time** for the **OANW** condition.
* The **NA** control condition is repeated **20 times**.
* **Total trials:** 100 trials per participant.

#### Phase 2:
* Each of the 20 real words is presented **2 times** for the **CAW** condition and **2 times** for the **OAW** condition.
* Each of the 20 nonce words is presented **2 times** for the **CANW** condition and **2 times** for the **OANW** condition.
* The **NA** control condition is repeated **40 times**.
* **Total trials:** 200 trials per participant.
