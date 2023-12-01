import mne
import numpy as np


# Set the logging level to ERROR (or CRITICAL)
mne.set_log_level("ERROR")

def readData(path, l_freq=0.5, h_freq=45, durartion=5, overlap=0):
    """
    1. This function reads the data
    2. set a reference
    3. filter the data
    4. segments the signals to equal number of epochs
    5. convert the data into numpy arrays

    parameter
    -----------
    path: str
    the path to the signal

    l_freq:float
    lower cutoff frequency

    h_freq:float
    high cutoff frequency

    durartion:int
    lenght of each epoch in seconds


    overlap=int
    amount of overlap between different epochs


    return
    ------------
    numpyArray: numpy array
    cleaned and segmented signal in numpy array format

    """

    data = mne.io.read_raw_eeglab(path)

    # By default the reference is the average of
    # all channels
    data.set_eeg_reference()

    # Filtering the data
    data.filter(l_freq=l_freq, h_freq=h_freq)

    # Segmenting the data into equal segments
    epochs = mne.make_fixed_length_epochs(data, 
                                    duration=durartion,
                                    overlap=overlap)

    # Till here, all the data are as mne objects
    # but using the bellow code, we convert the data
    # into numpy array
    numpyArray = epochs.get_data()

    return numpyArray
