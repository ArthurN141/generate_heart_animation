# generate_heart_animation

Generating a heart with words, using pygame and ffmpeg (python).
For all downloads, make sure you choose the corresponding extention OS (MacOs, Windows, Linux), for Apple there is a distinction of the CPU (Intel or Apple). If your Mac was bought before 2***, it mostly wont have Apple M1 cpu.

- Step 1 :
  Download python at : https://www.python.org/downloads/


- Step 2 :
  Imports the none natives python modules. If you want to use any music file codec (like .m4v), it's recommanded to download the app VLC at : https://www.videolan.org/vlc/
  Then, you have to open your terminal on MacOS or windows and enter theses commandes : (pour VlC et pygame pour chaque OS)
  You have to download the compiled code of ffmpeg if you want to generate a videso as well : https://ffmpeg.org/download.html\


- Step 3 :
 Once it's all done, create a new python file, copy the entire code from "main.py", save it, put the app ffmpeg at the same place (root) as the file.
 For the music, you need to determine the path, if you dont know it, you can drop the file on your terminal, it will show your the path, beware of escape symbole "\", you have to
 remove them (example : /your/file/path/this\ is\ the\ name.mp3 become : /your/file/path/this is the name.mp3). If the path is wrong of the file not existing, the code will
 automatically propose to choose a music file. If VLC is not installed or imported, the code will use the default module pygame.mixer from pygame.


- Step 4 :
  You can customize  and choose the words (WORDS and WORDS_COLOR_1, WORDS_COLOR_2...) and final center text (CENTER_TEXT) with colors (CENTER_COLOR_TEXT) as well as the
  BACKGROUND_COLOR, it accepts for example : RGB (01, 02, 03) value 0 to 255, decimal 123456 range 0 to 16777215 and hexadecimal
  0x34ff43 range 0x000000 to 0xffffff. You can write in string ("") name of colors like for example "Red", the list of the names are in COLOR_TEMPLATE.
  Each time you generate a video, the default runninng time is 35 seconds, you can change it with RUNNING_TIME, if you escape or close the window before, it will automatically
  stop the program. The video file generated is name "heart_animation.mp4", if there is already one existing, the program will create a new one named "heart_animation_2.mp4"
  and then "heart_animation_3.mp4" etc. If there is any error or issue while running the code, you will mostly see it explained on the console.
