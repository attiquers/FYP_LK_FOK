import asyncio
import logging
from livekit import rtc
from livekit.agents import JobContext, AgentSession, Agent, cli, WorkerOptions
from livekit.plugins import silero, openai
from livekit.plugins.turn_detector.english import EnglishModel

# Custom TTS & STT
from tts import KokoroTTS
from stt import WhisperSTT

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

class MyAssistant(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful local voice assistant. Keep answers short.")

async def entrypoint(ctx: JobContext):
    # Initialize STT and TTS
    
    stt_impl=WhisperSTT(
        model="jkawamoto/whisper-tiny-ct2",
        language="en",
        device="cpu",
        compute_type="float",
        # warmup_audio="./sample_audio.wav",  # 5-10 for warmup
    )

    tts_impl = KokoroTTS(
        base_url="http://localhost:8880/v1",
        api_key="NULL",
        voice="af_heart",
        speed=1.0
    )

    # LLM
    llm_impl = openai.LLM.with_ollama(
        model="gemma3:1b",
        base_url="http://localhost:11434/v1"
    )

    # VAD + turn detection
    vad_impl = silero.VAD.load()
    turn_detector = EnglishModel()

    # Create agent session
    session = AgentSession(
        vad=vad_impl,
        stt=stt_impl,
        llm=llm_impl,
        tts=tts_impl,
        turn_detection=turn_detector,
    )

    # Connect to room
    await ctx.connect()
    assistant = MyAssistant()

    # Start session
    await session.start(
        room=ctx.room,
        agent=assistant
    )

    await session.say("Hello! I'm ready to help. Please speak into your microphone.")

    logging.info("Voice assistant ready – speak into your microphone.")
    await asyncio.sleep(3600)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
