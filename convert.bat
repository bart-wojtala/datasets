for %%a in ("*.*") do ffmpeg -i "%%a" -ac 1 -ar 22050 "output\%%a"
pause