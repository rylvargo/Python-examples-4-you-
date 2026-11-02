#--------------------------------------------------------------------------------------------------------------|
# SOUNDDEVICE IMPORT
#--------------------------------------------------------------------------------------------------------------|

# INSTALL: Open your terminal and type:
# pip install sounddevice

import sounddevice as sd

print(sd.query_devices())  # Shows audio devices


#--------------------------------------------------------------------------------------------------------------|
#  Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----Example-----|
#--------------------------------------------------------------------------------------------------------------|


import sounddevice as sd

# Recording settings
duration = 5
sample_rate = 44100

print("Recording for 5 seconds...")

# Record audio
recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

# Wait for recording to finish
sd.wait()

print("Recording finished!")

# Play recording
sd.play(recording, sample_rate)
sd.wait()