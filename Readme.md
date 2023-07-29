## Vult: Batch video compression | transcoding utility
Vult is a CLI application that helps you batch compress videos in a directory for space optimization or decoder compatibility purposes.
Runs on any terminal either with a reactive TUI using [Textual](https://github.com/textualize/textual) or through `--headless` mode, 
written in Python, and runs on both Windows and Linux-based operating systems

---
### 📢 Warning: This is a work in progress, and is by no means a functional tool yet. Currently working on developing simpler to use custom textual widgets alongside this project, which is what's mostly occupying development time, and will most likely receive its own repository in the future 📢
---

## ⚀ Dependencies:
- [Textual](https://github.com/textualize/textual): TUI library
- [FFmpeg](https:ffmpeg.com): Core application used for video encoding / decoding
- [xxHash](https:xxhash.com): Hash implementation for cross referencing & comparing in|out video sizes & resolving duplicates
- A terminal that supports UTF-8 and Ligatures, preferrably ones that use [Nerd Fonts](https://nerdfonts.com)

## ⚀ Features:
- **Format Agnostic**: **Automatically** adjusts encoding / decoding parameters for different video formats in the source dir
- **Simple**: Default TUI offers only a handful of parameters. Only worry about what's **important**
- **Presets**: Define **presets** in the TUI for quick and easy batch processing without having to touch the knobs
- **On Point**: A **no nonsense** Terminal User Interface. Dump your videos in, wait for it to come out
- **Flexible**: Offers both a **visual TUI** for cli enjoyers, and a **headless mode** for users who just want to get the job done
- **Small**: **Less than 1k LOCs**. The modular architecture allows easy customization of the UI, or for simple plugin / extension development

## ⚀ Supported Source File Formats:
- **MPEG4**[.mp4]
- **QuickTime**[.mov]
- **Matryoska**[.mkv]
- **AV1**[.avi]

## ⚀ Supported Output File Formats:
- **MPEG4**[.mp4]
- **QuickTime**[.mov]
- **Matryoska**[.mkv]
- ~~**AV1**[.avi]~~ *removed because haha slow*
