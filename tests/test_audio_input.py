from unittest.mock import patch, MagicMock
import core.audio_input as ai

def test_record_audio_mock(tmp_path):
    fake_file = tmp_path / "fake.wav"

    with patch("core.audio_input.pyaudio.PyAudio") as MockPyAudio:
        mock_p = MagicMock()
        MockPyAudio.return_value = mock_p

        # Mock stream
        mock_stream = MagicMock()
        mock_p.open.return_value = mock_stream
        mock_stream.read.return_value = b"\x00\x01" * 1024

        # 🧩 Mock get_sample_size to return 2 bytes (16 bits)
        mock_p.get_sample_size.return_value = 2

        result = ai.record_audio(duration=1, filename=str(fake_file))
        assert fake_file.exists()
        assert result.endswith(".wav")
