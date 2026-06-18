#!/usr/bin/env python3
"""Render figma-plugin/marketing/walkthrough.mp4 (1920x1080, H.264) from the
carousel slides, with crossfades. Uses the ffmpeg binary bundled by imageio-ffmpeg,
so no system ffmpeg is required:  pip install --user imageio-ffmpeg
"""
import os
import subprocess
import imageio_ffmpeg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MK = os.path.join(ROOT, "figma-plugin", "marketing")
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

N = 9            # carousel-1..9
DUR = 2.2        # seconds each slide is on screen
TRANS = 0.6      # crossfade duration

# inputs: each PNG held for DUR seconds
inputs = []
for i in range(1, N + 1):
    inputs += ["-loop", "1", "-t", str(DUR), "-i", os.path.join(MK, "carousel-%d.png" % i)]

# normalize each input, then chain xfade transitions
parts = []
for i in range(N):
    parts.append(
        "[%d:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,format=yuv420p[s%d]" % (i, i)
    )
prev, off = "s0", DUR - TRANS
for i in range(1, N):
    out = "vout" if i == N - 1 else "x%d" % i
    parts.append("[%s][s%d]xfade=transition=fade:duration=%s:offset=%.3f[%s]"
                 % (prev, i, TRANS, off, out))
    prev = out
    off += DUR - TRANS
filt = ";".join(parts)

out = os.path.join(MK, "walkthrough.mp4")
cmd = [FFMPEG, "-y", *inputs,
       "-filter_complex", filt, "-map", "[vout]",
       "-c:v", "libx264", "-profile:v", "high", "-crf", "20", "-preset", "medium",
       "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-r", "30", out]
print("Encoding walkthrough.mp4 …")
subprocess.run(cmd, check=True, capture_output=True)
print("walkthrough.mp4:", os.path.getsize(out) // 1024, "KB")
