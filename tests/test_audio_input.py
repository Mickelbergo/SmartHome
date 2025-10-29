from unittest.mock import patch, MagicMock
from core import audio_input as ai
def test_record_audio_mock(tmp_data_dir):
    fake_file = tmp_data_dir / "fake.wav"

    with patch("core.audio_input.pyaudio.PyAudio") as MockPyAudio:
        mock_p = MagicMock()
        MockPyAudio.return_value = mock_p
        mock_stream = MagicMock()
        mock_p.open.return_value = mock_stream
        mock_stream.read.return_value = b"\x00\x01" * 1024

        result = ai.record_audio(duration=1, filename=fake_file)
        assert fake_file.exists()
        assert result.endswith(".wav")
