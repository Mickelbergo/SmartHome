import pyaudio, wave

def record_audio(filename="data/input.wav" , duration=5) -> str:

    """
    Records audio from the microphone and saves it to a WAV file.
    Args:
        filename (str): The name of the output WAV file
        duration (int): The duration of the recording in seconds
        
        
    Returns:
    
        str: The path to the saved WAV file
        
    """
    p = pyaudio.PyAudio()
    
    #whisper expects a rate of 16000, input = True opens the stream for recording
    #frames_per_buffer: number of samples to read per chunk, smaller buffer = lower latency but more CPU load -> try out lower buffer if latency too high
    stream = p.open(format = pyaudio.paInt16, channels=1, rate = 16000, input = True, frames_per_buffer=1024)
    
    frames = []
    
    #records for 5 seconds with 16000 / 1024 ≈ 15 chunks per second
    for _ in range(0, int((16000 / 1024) * duration)):
        frames.append(stream.read(1024))
        
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # 'wb' = write binary mode
    with wave.open(filename, "wb") as wf:

        wf.setnchannels(1) #mono audio
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16)) #paInt16 is 2 bytes per sample
        wf.setframerate(16000) #must match recording rate
        wf.writeframes(b''.join(frames)) #join in binary mode
        
    return filename