from livekit.agents import stt
from faster_whisper import WhisperModel
from pathlib import Path

MODEL_DIR = Path("models").resolve()

class CT2WhisperSTT(stt.STT):
    def __init__(self):
        super().__init__(capabilities=stt.STTCapabilities(
            streaming=False,  # only supports offline
            interim_results=False
        ))
        self.model = WhisperModel(
            model_size_or_path=str(MODEL_DIR),
            local_files_only=True,
            device="cpu",
            compute_type="int8"
        )

    async def _recognize_impl(self, audio, *, language="en"):
        segments, _ = self.model.transcribe(
            audio,
            language=language,
            vad_filter=False
        )
        for seg in segments:
            yield stt.SpeechEvent(
                type=stt.SpeechEventType.FINAL_TRANSCRIPT,
                alternatives=[stt.SpeechData(text=seg.text)]
            )
