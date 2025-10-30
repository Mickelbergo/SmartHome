from unittest.mock import patch
from core import speech_to_text as st

#mocks the transcribe audio
@patch("core.speech_to_text.model.transcribe", return_value = {"text": "hello world"})
def test_transcribe_audio(mock_transcribe: str) -> str:

    text = st.transcribe_audio("fake.wav")
    assert text == "hello world"
    mock_transcribe.assert_called_once_with("fake.wav")