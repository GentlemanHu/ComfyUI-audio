# ComfyUI-audio

generative audio tools for ComfyUI. highly experimental&mdash;expect things to break and/or change frequently or not at all.

**NOTE**: for the foreseeable future, i will be unable to continue working on this extension. please consider forking this repository!


## features
- [tacotron2 text-to-speech](https://github.com/NVIDIA/tacotron2)
    - uses justinjohn0306's forks of [tacotron2](https://github.com/justinjohn0306/TTS-TT2/) and [hifi-gan](https://github.com/justinjohn0306/hifi-gan/)
- [musicgen text-to-music + audiogen text-to-sound](https://facebookresearch.github.io/audiocraft/docs/MUSICGEN.html)
    - audiocraft and transformers implementations
    - supports audio continuation, unconditional generation
- [tortoise text-to-speech](https://github.com/neonbjb/tortoise-tts)
- [vall-e x text-to-speech](https://github.com/Plachtaa/VALL-E-X)
    - uses [korakoe's fork](https://github.com/korakoe/VALL-E-X)
- [voicefixer](https://github.com/voicefixer/voicefixer)
- audio utility nodes
    - save audio, convert audio

## installation
```shell
# TORCH_CUDA_INDEX_URL=https://download.pytorch.org/whl/cu118  # for cuda 11.8
TORCH_CUDA_INDEX_URL=https://download.pytorch.org/whl/cu121  # for cuda 12.1

cd ComfyUI/custom_nodes
git clone https://github.com/eigenpunk/ComfyUI-audio
cd ComfyUI-audio

# for linux
pip install -r requirements.txt --extra-index-url $TORCH_CUDA_INDEX_URL

# for windows
pip install -r requirements_windows.txt --extra-index-url $TORCH_CUDA_INDEX_URL
```

this extension is developed and tested on a Linux-based OS. i've not yet been able to get the extension fully working on Windows, so
expect some difficulty if that is your platform. i've not tested the extension on macOS at all.

## would be nice to have maybe
- audio uploads
- audio previews
- prompt weights for text-to-music/audio
- stereo musicgen
- multi-band diffusion
- more/faster tts model support
    - [vits](https://huggingface.co/docs/transformers/model_doc/vits)?
    - ~~[tacotron2](https://github.com/NVIDIA/tacotron2)~~
    - ~~[vall-e x](https://github.com/Plachtaa/VALL-E-X)~~
    - ???
- split generator nodes by model stages
    - e.g. tortoise:
        - autoregressor
        - clvp/cvvp
        - spectrogram diffusion
    - e.g. musicgen:
        - t5 text encode
        - encodec audio encode
        - generate with decoder
- more audio generation models
    - magnet, etc
- demucs
- ~~audiogen~~


*NOTE*: this work is solely a personal project; its development is not supported/sponsored by any past/present employer or any other external organization.
