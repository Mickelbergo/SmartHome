import whisper

from utils.logger import get_logger

logger = get_logger(__name__)
model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    """Transcribe a .wav file to text using local whisper"""

    try: 
        logger.info(f'Transcribing audio {audio_path}')
        result = model.transcribe(audio_path)
        text = result.get("text", "").strip()
        logger.info(f'Transcription: {text}')
        return text
    except Exception as e:
        logger.error(f'Transcription failed: {e}')
        return ""
    
