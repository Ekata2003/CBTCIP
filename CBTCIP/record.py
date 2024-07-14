import sounddevice as sd
import wavio


def record_audio(duration, filename, samplerate=44100):
    print("Recording...")
    # Record audio for the given duration
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")

    # Save the recording to a WAV file
    wavio.write(filename, recording, samplerate, sampwidth=2)
    print(f"Recording saved to {filename}")


# Example usage
record_duration = 5  # Duration in seconds
output_filename = "recording.wav"

record_audio(record_duration, output_filename)
