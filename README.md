cd services/kokorofastapi/docker/cpu
docker compuse up --build

then to re-run
docker compuse up 




Backend
+ Users relation in between entinties and user is stored in NEO4J graph 
+ For each edge the data needs to be stored in SQL DB with primary key = Entit1-Entity2
- Users grammer mistakes, sensible WER, audios, summaries
- It can join google meets, zoom meetings as assitant like Dan used Fathom in my meeting


Current Task:
- Connect livekit to local models
    - Full (with avatar): https://github.com/dwain-barnes/simli-kokoro-whisper-livekit
    - Reddit post: https://www.reddit.com/r/LocalLLaMA/comments/1kbj97u/local_private_voice_agent_via_ollama_kokoro/
    
    - Whisper plugin: https://github.com/atyenoria/livekit-whisper-transcribe
    - Kokoro plugin: https://github.com/taresh18/livekit-kokoro
    + Ollama plugin: https://docs.livekit.io/agents/integrations/llm/ollama/

    * Ollama:
        - LLM: https://ollama.com/library/gemma3
        - maybe we have to use tool calling once try those too
    * Use models from hugginface: https://huggingface.co/models
        - STT:
            * https://huggingface.co/openai/whisper-large-v3-turbo/tree/main
            * https://huggingface.co/Systran/faster-whisper-large-v3
            * huggingface.co/mobiuslabsgmbh/faster-whisper-large-v3-turbo
            * https://huggingface.co/pyannote/speaker-diarization-3.1
        - TTS:
            * https://huggingface.co/hexgrad/Kokoro-82M [mix their own voices]
            * https://huggingface.co/ResembleAI/chatterbox/tree/main [voice clone]
            * https://huggingface.co/microsoft/VibeVoice-1.5B [voice clone?]
            * https://huggingface.co/coqui/XTTS-v2 [voice clone, heard alot]
            * https://huggingface.co/sesame/csm-1b [very realistic, cloning allowed]
            https://www.youtube.com/watch?v=220XKBzIp2U&t=961s



- Reduce Noise
- Connect the livekit room to flutter app client, while agent waits on laptop for user to connect to a room
- Call logs added into logger-DATE-TIME with last log as summary of convo
+ Turn Detection: Livekit plugins
    + SileroVAD
    + EnglishTurnDetection Model