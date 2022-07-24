md output
for %%a in ("*.*") do ffmpeg-normalize "%%a" -nt peak -t -1.0 -o "output\%%a"
pause
