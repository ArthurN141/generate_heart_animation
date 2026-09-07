# generate_heart_animation

Generate a heart-shaped animation made of words using **Python, Pygame and FFmpeg**.

## Requirements

* Python 3
* Pygame
* FFmpeg *(optional, only required if you want to generate a video)*
* VLC *(optional, recommended for additional audio format support)*

> **Apple Silicon Macs:** if you have a Mac with an Apple M1, M2, M3, M4, etc. chip, you need the **Apple Silicon / ARM64** version of the corresponding software.
>
> The first Apple Silicon Mac was released in **November 2020**. If your Mac was purchased before 2020, it will most likely have an Intel processor.
>
> To check your Mac's processor, open **Apple menu → About This Mac**. It will indicate either an **Intel** processor or an **Apple M-series** chip.

---

## Step 1 — Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

Make sure Python is available from your terminal.

You can check it with:

```bash
python3 --version
```

On Windows, you can also try:

```bash
python --version
```

---

## Step 2 — Install the Python modules

Open your terminal (**Terminal** on macOS/Linux or **Command Prompt / PowerShell** on Windows) and run:

```bash
python3 -m pip install pygame python-vlc
```

On Windows, if `python3` is not recognized, use:

```bash
python -m pip install pygame python-vlc
```

### VLC

VLC is **not required** to run the program, but it is recommended if you want to use audio formats that may not be supported reliably by `pygame.mixer` (for example, `.m4a`).

Download VLC from:

https://www.videolan.org/vlc/

Install the version corresponding to your operating system and CPU architecture.

If VLC is not installed, or if the Python `vlc` module cannot be used, the program will automatically fall back to `pygame.mixer`.

---

## Step 3 — Install FFmpeg

FFmpeg is **optional**.

You only need it if you want the program to generate an `.mp4` video.

Download FFmpeg from:

https://ffmpeg.org/download.html

You must download a **pre-compiled FFmpeg binary** corresponding to your operating system and CPU architecture.

For example, on a Mac:

* **Intel Mac** → download the Intel / x86_64 version
* **Apple Silicon Mac (M1/M2/M3/M4...)** → download the Apple Silicon / ARM64 version

Once downloaded, place the FFmpeg executable in the **same directory as the Python file**.

The program expects it to be named:

```text
ffmpeg
```

on macOS/Linux, or the appropriate executable name on Windows.

If FFmpeg is not found, the animation will still run normally, but no video will be generated.

---

## Step 4 — Run the program

Create a Python file and copy the complete code from `main.py` into it.

Save the file in a folder of your choice.

The FFmpeg executable must be placed in the **same folder** as the Python file.

Your folder should look approximately like this:

```text
Your folder/
├── main.py
└── ffmpeg
```

### Music file

You can configure the path to your music file directly in the Python code.

If you do not know the path:

1. Open your terminal.
2. Drag and drop the music file into the terminal.
3. The full path will appear automatically.

On macOS, the terminal may add backslashes (`\`) before spaces or special characters.

For example:

```text
/Users/Arthur/My\ Music/song.mp3
```

should be written in the Python configuration as:

```text
/Users/Arthur/My Music/song.mp3
```

If the configured path is invalid or the file does not exist, the program will automatically open a file picker and ask you to select a music file.

---

## Step 5 — Customize the animation

You can customize the animation directly from the configuration section of the Python file.

### Words

You can change the words displayed around the heart with:

```python
WORDS
```

Each word can have its own color:

```python
WORDS_COLOR_1
WORDS_COLOR_2
WORDS_COLOR_3
WORDS_COLOR_4
WORDS_COLOR_5
```

### Center text

The final text displayed in the center of the heart can be changed with:

```python
CENTER_TEXT
```

Its color can be changed with:

```python
CENTER_COLOR_TEXT
```

### Background

The background color can be changed with:

```python
BACKGROUND_COLOR
```

### Supported color formats

Colors can be specified using several different formats.

#### RGB

Values must be between `0` and `255`:

```python
(255, 0, 0)
```

#### Decimal

The value must be between `0` and `16777215`:

```python
123456
```

#### Hexadecimal

Using `0x`:

```python
0x34ff43
```

Range:

```text
0x000000 → 0xffffff
```

#### Color names

You can also use a color name as a string:

```python
"Red"
```

Color names are **case-insensitive**, so these are equivalent:

```python
"Red"
"red"
"RED"
```

The available color names are listed in:

```python
COLOR_TEMPLATE
```

---

## Running time

The default animation running time is **35 seconds**.

You can change it with:

```python
RUNNING_TIME
```

You can also stop the program manually at any time by:

* closing the window, or
* pressing `Escape`.

---

## Generated video files

When FFmpeg is available, the program automatically generates an MP4 video.

The first video will be named:

```text
heart_animation.mp4
```

If a file with that name already exists, the program will **not overwrite it**.

Instead, it will create:

```text
heart_animation_2.mp4
```

Then:

```text
heart_animation_3.mp4
```

and so on.

This allows you to keep multiple versions of your animation.

---

## Program statistics

When the program finishes, it displays statistics such as:

```text
Program duration : 33.24 sec
Real FPS         : 46.60 FPS
Target FPS       : 60 FPS
Video duration   : 25.82 sec
Time ratio       : 1.287
```

These values can be used to compare the actual performance of the computer with the target FPS.

A **Time ratio closer to `1.000`** means that the program was able to stay closer to the configured target FPS.

---

## Troubleshooting

If something goes wrong while running the program, check the terminal/console first.

The program is designed to display warnings and errors there to help identify the problem.

If FFmpeg is missing, the animation can still run without generating a video.

If VLC is missing or cannot be used, the program will automatically fall back to `pygame.mixer`.

---

## Getting the project

You can download or clone this project directly from GitHub.

### Using Git

If Git is installed on your computer, open a terminal and run:

```bash
git clone https://github.com/ArthurN141/generate_heart_animation.git
```

Then enter the project directory:

```bash
cd generate_heart_animation
```

### Without Git

You can also download the project directly from GitHub by clicking:

**Code → Download ZIP**

Then extract the ZIP file wherever you want.

---

## License

*Copyright (c) 2026 Arthur Neuss
MIT License*

---

## Disclaimer

This project is an enhanced version of an existing codebase. It originally started as a TikTok trend, and I sourced the initial code from GitHub 
(such as [this repository](https://github.com/YoBoiMarvs/BlueHeart), though its original authorship and licensing remain unclear as identical code exists across multiple repositories).

**What I changed:**
The original code was unoptimized and appeared to be largely AI-generated without prior review (99% vibecoded). I have significantly refactored, 
optimized, and rewritten major parts of it to make it user-friendly, stable, and production-ready.

