# ➤ Native Python imports
import math
import random
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import platform
import subprocess
import os
import time
# ➤ Other imports
try:
    import vlc
    VLC_AVAILABLE = True
except ImportError:
    VLC_AVAILABLE = False

try:
    import pygame
except ImportError:
    print("❌ Pygame is not installed.")
    print()
    print("Please install it from your terminal with the following command.")
    print()
    if platform.system() == "Darwin":
        print("On MacOs, copy and paste this :")
        print("    python3 -m pip install pygame")
    elif platform.system() == "Windows":       
        print("On Windows, copy and paste this :")
        print("    python -m pip install pygame")
    else:
        print("Other OS, copy and paste this :")
        print("    python3 -m pip install pygame")

    print()
    print(
        "A terminal window will now be opened for you, "
        "copy the command and press enter, then run the programe again !"
    )
    if platform.system() == "Darwin":
        subprocess.Popen(["open", "-a", "Terminal"])

    elif platform.system() == "Windows":
        try:
            subprocess.Popen(["wt"])
        except FileNotFoundError:
            subprocess.Popen(["cmd"])

    raise SystemExit(1) 


BASE_DIR = Path(__file__).resolve().parent
FFMPEG_PATH = BASE_DIR / "ffmpeg" # ➤ Needed to save the animation to .mp4
VIDEO_PATH = BASE_DIR / "heart_animation.mp4" # ➤ You can change the file name but you have to leave .mp4 at the end !
MUSIC_PATH = Path.home() / "Your/Music/Path/Here/File Name.m4a" # ➤ Put the music path here.


# ➤ You can edit all colors with RGB, decimal or hexadecimal, or preset colors names listed in : COLOR_TEMPLATE (line 76).
BACKGROUND_COLOR = (0, 0, 0) # ➤ It's black 
FPS = 60 # ➤ Frame generated per second, your computer might not be able to handle this, there will be a recap of the actual frame rate at the end.
RUNNING_TIME = 35 # ➤ The time the animation is running (in seconds).

CENTER_TEXT = " Your Text Here" # ➤ It's the final phrase displayed at the end.
CENTER_COLOR_TEXT = (255, 250, 245) # ➤ It's 99% white here

WORDS = ["first word here", "First Word Here", "FIRST WORD HERE"] # ➤ You can add or remove strings
# ➤ Colors your words will have
WORDS_COLOR_1 = (70, 130, 180)
WORDS_COLOR_2 = (30, 144, 255)
WORDS_COLOR_3 = (0, 191, 255)
WORDS_COLOR_4 = (100, 149, 237)
WORDS_COLOR_5 = (65, 105, 225)


# ➤ Default colors name, you can put then in strings after a value, for example WORDS_COLOR_1 = "Green".
COLOR_TEMPLATE = {
    "Red": 0xed4245,
    "Orange": 0xff8800,
    "Yellow": 0xfee75c,
    "Green": 0x57f287,
    "Blurple": 0x5865f2,
    "Purple": 0x9b59b6,
    "Off White": 0xbcc0c0,
    "Dark Gray": 0x2c2f33,
    "Cyan": 0x00ffff,
    "Pink": 0xff80ed,
    "Pastel Gray": 0xa3a3a3,
    "Pastel Pink": 0xf8bbd0,
    "Glacier Blue": 0xa0d9ff,
    "Light Lavender": 0xcbaacb,
    "Pastel Peach": 0xffdab9,
    "Matcha Green": 0xbee3a1,
    "Soft Mint": 0xb4f8c8,
    "Neon Blue": 0x00e5ff,
    "Electric Purple": 0xd46ffb,
    "Pastel Yellow": 0xfff9b0,
}

COLOR_NAMES = {
    name.lower(): value
    for name, value in COLOR_TEMPLATE.items()
}

def to_rgb(color, color_name="Color"):
    # ➤ RGB tuple / list
    if isinstance(color, (tuple, list)):
        if (
            len(color) == 3
            and all(isinstance(x, int) and not isinstance(x, bool) for x in color)
            and all(0 <= x <= 255 for x in color)
        ):
            return tuple(color)
    # ➤ Decimal integer
    elif isinstance(color, int) and not isinstance(color, bool):
        if 0 <= color <= 0xFFFFFF:
            return (
                (color >> 16) & 0xFF,
                (color >> 8) & 0xFF,
                color & 0xFF
            )
    # ➤ Colors names        
    elif isinstance(color, str):
        value = color.strip()
        # Color name
        if value.lower() in COLOR_NAMES:
            decimal = COLOR_NAMES[value.lower()]
            return (
                (decimal >> 16) & 0xFF,
                (decimal >> 8) & 0xFF,
                decimal & 0xFF
            )
        # ➤ Hexadecimal
        hex_value = value.lower()
        if hex_value.startswith("0x"):
            hex_value = hex_value[2:]

        if len(hex_value) == 6:
            try:
                decimal = int(hex_value, 16)

                return (
                    (decimal >> 16) & 0xFF,
                    (decimal >> 8) & 0xFF,
                    decimal & 0xFF
                )
            except ValueError:
                pass

    print(f"\n⚠️ {color_name} : {color!r} is not a valid color format.")
    print("\nAccepted formats and examples :")
    print("  • RGB       → (1, 2, 3) (Value : 0 to 255)")
    print("  • Decimal   → 123456 (Range : 0 to 16777215)")
    print("  • Hex       → 0x34ff43 (Range : 0x000000 to 0xffffff")
    print("  • Color name → Red (case insensitive)")
    print()
    print("Available color names :")
    print("  " + ", ".join(COLOR_TEMPLATE.keys()))
    return None


# ➤ Audio extensions supported
AUDIO_EXTENSIONS = {
    ".mp3", ".wav", ".ogg", ".oga", ".flac", ".m4a", ".aac",
    ".wma", ".aiff", ".aif",
}

def choose_music_file():
    root = tk.Tk()
    root.withdraw()

    while True:
        file_path = filedialog.askopenfilename(
            title="Select an audio file",
            filetypes=[
                (
                    "Audio files",
                    "*.mp3 *.wav *.ogg *.oga *.flac "
                    "*.m4a *.aac *.wma *.aiff *.aif"
                ),
                ("All files", "*.*"),
            ],
        )
        if not file_path:
            root.destroy()
            return None

        path = Path(file_path)
        if path.suffix.lower() in AUDIO_EXTENSIONS:
            root.destroy()
            return path

        print(
            f"\n⚠️ '{path.name}' doesn't appear to be a supported audio file."
        )
        print("Please select an audio file.")



SIZE_MULT = [0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15] # ➤ It's not recommanded to change theses values.
class Particle:
    __slots__ = (
        'x', 'y', 'order', 'kind', 'word', 'color',
        'alpha', 'flicker', 'font', 'delay', 'size_mult'
    ) 
    def __init__(self, x, y, order, kind, colors_text):
        self.x = x
        self.y = y
        self.order = order
        self.kind = kind
        self.word = random.choice(WORDS)
        self.color = random.choice(colors_text)
        self.alpha = 0
        self.flicker = random.uniform(0, math.pi * 2)
        self.font = None
        self.delay = 0
        self.size_mult = random.choice(SIZE_MULT)


def heart_xy(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, -y


def to_screen(x, y, scale, width, height):
    return x * scale + width / 2, y * scale + height / 2 


def build_outline_particles(n_outline, min_gap=30, scale=1, width=0, height=0, colors_text=None):
    particles = []
    placed = []
    for i in range(n_outline):
        t = (i / n_outline) * 2 * math.pi
        bx, by = heart_xy(t)
        sx, sy = to_screen(bx, by, scale, width, height)
        if any(math.hypot(sx - px, sy - py) < min_gap for (px, py) in placed):
            continue
        placed.append((sx, sy))
        particles.append(Particle(sx, sy, i, "outline", colors_text))
    return particles


def build_fill_particles(n_fill, min_gap=46, scale=1, width=0, height=0, colors_text=None):
    particles = []
    placed = []
    attempts = 0
    max_attempts = n_fill * 80
    
    while len(particles) < n_fill and attempts < max_attempts:
        attempts += 1
        t = random.uniform(0, 2 * math.pi)
        r = random.uniform(0.0, 0.86)
        bx, by = heart_xy(t)
        px, py = bx * r, by * r
        sx, sy = to_screen(px, py, scale, width, height)
        
        if any(math.hypot(sx - qx, sy - qy) < min_gap for (qx, qy) in placed):
            continue
            
        placed.append((sx, sy))
        particles.append(Particle(sx, sy, random.randint(0, 320), "fill", colors_text))
    
    return particles


def draw_glow_text(glow_layer, screen_layer, rendered, x, y, alpha):
    if alpha <= 0:
        return

    txt, glow_big, glow_small = rendered
    txt.set_alpha(alpha)

    if alpha > 10:
        glow_big.set_alpha(alpha // 7)
        glow_small.set_alpha(alpha // 3)

        glow_layer.blit(
            glow_big,
            glow_big.get_rect(center=(x, y))
        )
        glow_layer.blit(
            glow_small,
            glow_small.get_rect(center=(x, y))
        )
    screen_layer.blit(
        txt,
        txt.get_rect(center=(x, y))
    )


def get_unique_video_path(base_path):
    if not base_path.exists():
        return base_path

    counter = 2
    while True:
        new_path = base_path.with_name(
            f"{base_path.stem}_{counter}{base_path.suffix}"
        )
        if not new_path.exists():
            return new_path

        counter += 1 


# ➤ Main function to make it all run
def main():
    # ➤ Colors format verification
    background_color = to_rgb(
        BACKGROUND_COLOR,
        "BACKGROUND_COLOR"
    )
    center_color = to_rgb(
        CENTER_COLOR_TEXT,
        "CENTER_COLOR_TEXT"
    )
    colors_text = [
        to_rgb(WORDS_COLOR_1, "WORDS_COLOR_1"),
        to_rgb(WORDS_COLOR_2, "WORDS_COLOR_2"),
        to_rgb(WORDS_COLOR_3, "WORDS_COLOR_3"),
        to_rgb(WORDS_COLOR_4, "WORDS_COLOR_4"),
        to_rgb(WORDS_COLOR_5, "WORDS_COLOR_5")
    ]
    if (
        background_color is None
        or center_color is None
        or any(color is None for color in colors_text)
    ):
        return
    # ➤ Music path verification
    music_file = MUSIC_PATH
    if music_file is None or not Path(music_file).is_file():
        print("\n⚠️ The configured music file could not be found.")
        print("Please select an audio file.")

        music_file = choose_music_file()
        if music_file is None:
            print("\n❌ No audio file selected. Exiting.")
            return
    # ➤ Shows the music path
    print(f"\nAudio file : {music_file}")
    
    pygame.init()
    # ➤ window init
    screen = pygame.display.set_mode((0, 0), pygame.DOUBLEBUF)
    WIDTH, HEIGHT = screen.get_size()
    SCALE = min(WIDTH, HEIGHT) * 0.025
    pygame.display.set_caption("Heart Animation") # ➤ You can edit the name
    # ➤ VLC check
    player = None  
    if VLC_AVAILABLE:
        try:
            player = vlc.MediaPlayer(str(music_file))
            player.play()
        except Exception as e:
            print(f"\n⚠️ VLC couldn't be used : {e}")
            player = None
    
    if player is None:
        print("\nAlternative solution used : pygame.mixer")
        print(
            "VLC is heavily recommended because it supports more audio codecs."
        )
        print("\nDownload VLC : https://www.videolan.org/vlc/")
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(str(music_file))
            pygame.mixer.music.play()
        except Exception as e:
            print(f"\n❌ Pygame couldn't play this audio file: {e}")
            pygame.quit()
            return
    # ➤ Fonts
    font_outline = pygame.font.SysFont("arial", 20, bold=True)
    font_fill = pygame.font.SysFont("arial", 17, bold=True)
    font_center = pygame.font.SysFont("georgia", 54, bold=True)
    center_base = font_center.render(
        CENTER_TEXT,
        True,
        center_color
    )
    center_cache = {}
    
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(background_color)
    
    outline = build_outline_particles(
        n_outline=160, scale=SCALE, width=WIDTH, height=HEIGHT, colors_text=colors_text
    )
    fill = build_fill_particles(
        n_fill=130, scale=SCALE, width=WIDTH, height=HEIGHT, colors_text=colors_text
    )  
    outline_span = max(p.order for p in outline) if outline else 0
    frames_per_step = 1.6
    fill_start_frame = int(outline_span * frames_per_step) + 30
    
    for p in fill:
        p.delay = fill_start_frame + p.order
    for p in outline:
        p.delay = int(p.order * frames_per_step)

    particles = outline + fill
    for p in particles:
        p.font = font_outline if p.kind == "outline" else font_fill
        
    text_cache = {}
    for p in particles:
        key = p.kind, p.word, p.color, p.size_mult
        if key in text_cache:
            continue
        
        if p.size_mult != 1.0:
            font_size = int(p.font.get_height() * p.size_mult)
            render_font = pygame.font.Font(None, font_size)
        else:
            render_font = p.font

        txt = render_font.render(p.word, True, p.color)
        glow_big = pygame.transform.smoothscale(
            txt,
            (
                int(txt.get_width() * 2.4),
                int(txt.get_height() * 2.4)
            )
        )
        glow_small = pygame.transform.smoothscale(
            txt,
            (
                int(txt.get_width() * 1.6),
                int(txt.get_height() * 1.6)
            )
        )
        text_cache[key] = (txt, glow_big, glow_small)
    # ➤ Checking if ffmpeg is a file and is executable
    ffmpeg_available = FFMPEG_PATH.is_file() and os.access(FFMPEG_PATH, os.X_OK)
    if not ffmpeg_available:
        print("\n⚠️ FFmpeg was not found.")
        print("The animation will continue normally, but no video will be recorded.")
        print()
        print("To enable video recording: ")
        print("• Download FFmpeg for your operating system :")
        print("    https://ffmpeg.org/download.html\n")
        print("• Place the FFmpeg executable in the same folder as this Python file.")
        print("• Make sure 'ffmpeg' is the executable itself, not a folder.")
    # ➤ Recording
    ffmpeg = None
    if ffmpeg_available:
        video_path = get_unique_video_path(VIDEO_PATH)
        print(f"\n🎥 Output video : {video_path.name}")
        ffmpeg = subprocess.Popen(
            [
                str(FFMPEG_PATH),
                "-y",
                "-f", "rawvideo",
                "-vcodec", "rawvideo",
                "-pix_fmt", "rgb24",
                "-s", f"{WIDTH}x{HEIGHT}",
                "-framerate", str(FPS),
                "-i", "-",
                "-i", str(music_file),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-shortest",
                str(video_path),
            ],
            stdin=subprocess.PIPE,
        )
    running = True
    frame = 0
    start_time = time.perf_counter()
    glow_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    text_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    # ➤ Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        
        screen.blit(background, (0, 0))
        glow_layer.fill((0, 0, 0, 0))
        text_layer.fill((0, 0, 0, 0))
        frame += 1

        
        for p in particles:
            if frame > p.delay and p.alpha < 255:
                p.alpha = min(255, p.alpha + 14 + random.randint(0, 4))
            
            if p.alpha >= 255:
                flick = 0.75 + 0.25 * math.sin(frame * 0.04 + p.flicker)
            else:
                flick = 1.0
            
            alpha = int(p.alpha * flick)
            if alpha <= 0:
                continue

            rendered = text_cache[(p.kind, p.word, p.color, p.size_mult)]
            draw_glow_text(glow_layer, text_layer, rendered, 
                          p.x, p.y, alpha)
        
        screen.blit(glow_layer, (0, 0))
        screen.blit(text_layer, (0, 0))
        
        center_start = fill_start_frame + 200
        if frame > center_start:
            progress = min(1.0, (frame - center_start) / 60)
            center_alpha = int(255 * (1 - math.exp(-progress * 8)))
            
            pulse = 1.0 + 0.025 * math.sin(frame * 0.05)
            pulse_key = round(pulse, 3)
            cached = center_cache.get(pulse_key)
            if cached is None:
                center_surf = pygame.transform.smoothscale(
                    center_base,
                    (
                        int(center_base.get_width() * pulse_key),
                        int(center_base.get_height() * pulse_key)
                    )
                )
                glow_center = pygame.transform.smoothscale(
                    center_surf,
                    (
                        int(center_surf.get_width() * 1.4),
                        int(center_surf.get_height() * 1.4)
                    )
                )
                center_cache[pulse_key] = (
                    center_surf,
                    glow_center
                )
            else:
                center_surf, glow_center = cached

            center_surf.set_alpha(center_alpha)
            if center_alpha > 10:
                glow_center.set_alpha(center_alpha // 5)

                glow_rect = glow_center.get_rect(
                    center=(WIDTH / 2, HEIGHT / 2)
                )
                screen.blit(glow_center, glow_rect)

            text_rect = center_surf.get_rect(
                center=(WIDTH / 2, HEIGHT / 2)
            )
            screen.blit(center_surf, text_rect)          
        
        pygame.display.flip()
        
        if ffmpeg_available:
            frame_data = pygame.image.tostring(screen, "RGB")
            ffmpeg.stdin.write(frame_data)
        
        if time.perf_counter() - start_time >= RUNNING_TIME:
            running = False

    program_duration = time.perf_counter() - start_time
    # ➤ Closing of all module
    if ffmpeg_available:    
        ffmpeg.stdin.close()
        ffmpeg.wait()

    if player is not None:
        player.stop()
    else:
        pygame.mixer.music.stop()
        
    pygame.quit()
    # ➤ Final recap
    print("\n══════════════════════════════════════")
    print("           Program statistics")
    print("══════════════════════════════════════")
    print(f"Program duration : {program_duration:.2f} sec")
    # ➤ Real FPS = frames generated / real execution time
    real_fps = frame / program_duration if program_duration > 0 else 0
    print(f"Real FPS         : {real_fps:.2f} FPS")
    print(f"Target FPS       : {FPS} FPS")
    if ffmpeg_available:
        video_duration = frame / FPS
        time_ratio = (
            program_duration / video_duration
            if video_duration > 0
            else 0
        )
        print(f"Video duration   : {video_duration:.2f} sec")
        print(f"Time ratio       : {time_ratio:.3f}")
        print()
        print(
            "The difference between the program duration and the "
            "video duration is caused by the real FPS."
        )
        print(
            "The video is encoded at the target FPS, while the program "
            "may generate frames more slowly."
        )
        print(
            "A time ratio closer to 1.000 means that the computer "
            "was able to stay closer to the target FPS."
        )
    else:
        print("Video duration   : N/A (FFmpeg unavailable)")
        print("Time ratio       : N/A")

    print("══════════════════════════════════════")


# ➤ Run
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\nError occured :", e)
        import traceback
        traceback.print_exc()

