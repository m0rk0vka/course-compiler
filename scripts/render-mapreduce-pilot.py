import sys
import subprocess as s, tempfile, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
scenes=[
("The map task finishes","Worker A finishes a map task and stores two intermediate partitions on its local disk. Each reducer needs its own partition.","P1 and P2 ready","Idle","Waiting for P1","Waiting for P2"),
("One reducer gets its data","Reducer one fetches its partition from worker A. Reducer two has not fetched its partition yet.","Serving P1 and P2","Idle","Has P1 from A","Waiting for P2"),
("Worker A goes down","Worker A crashes. Its local files are now unreachable. Which reducer still needs data? Take a moment to predict what happens next.","Unreachable","Idle","Has P1 from A","Waiting for P2"),
("Retry the same map task","The coordinator assigns the same map task to worker B. Reducer two fetches its missing partition from B. Reducer one keeps the partition it already fetched.","Unreachable","P1 and P2 rebuilt","Keeps P1 from A","Has P2 from B"),
("Why this works","A deterministic map function produces equivalent intermediate data from the same input. Each reducer uses one partition per logical map task. Retrying the computation restores missing data without counting it twice.","Unreachable","Retry complete","Uses P1 once","Uses P2 once")]
def run(*args): s.run(args,check=True,stdout=s.DEVNULL)
def font(n,b=False):return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if b else '')+'.ttf',n)
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp)
 for i,(title,voice,*states) in enumerate(scenes):
  im=Image.new('RGB',(1280,720),'#101b2b');d=ImageDraw.Draw(im)
  d.text((64,45),'DISTRIBUTED SYSTEMS   /   MAPREDUCE',font=font(22,True),fill='#81dbca')
  d.text((64,87),title,font=font(49,True),fill='white')
  for j,(name,state) in enumerate(zip(['Worker A','Worker B','Reducer 1','Reducer 2'],states)):
   x=64+(j%2)*592;y=191+(j//2)*132
   d.rounded_rectangle((x,y,x+560,y+110),radius=15,fill='#1e3047')
   d.text((x+22,y+16),name,font=font(26,True),fill='white')
   d.text((x+22,y+57),state,font=font(24),fill='#ffb49c' if state=='Unreachable' else '#b9e8e0')
  d.rounded_rectangle((64,480,1216,638),radius=15,fill='#080f1b')
  d.multiline_text((89,503),textwrap.fill(voice,77),font=font(26),fill='white',spacing=9)
  d.text((64,666),f'{i+1} / 5    •    Dean & Ghemawat, MapReduce (2004), §3.3',font=font(20),fill='#b1c1d3')
  im.save(p/f'{i}.png')
  (p/f'{i}.txt').write_text(voice)
  run('ffmpeg','-v','error','-loop','1','-framerate','24','-i',str(p/f'{i}.png'),'-f','lavfi','-i',f'flite=textfile={p}/{i}.txt:voice=slt','-af',f'apad=pad_dur={5 if i==2 else 1}', '-shortest','-c:v','libx264','-threads','2','-pix_fmt','yuv420p','-c:a','aac',str(p/f'{i}.mp4'))
 (p/'list.txt').write_text(''.join(f"file '{i}.mp4'\n" for i in range(len(scenes))))
 run('ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(p/'list.txt'),'-c','copy','-movflags','+faststart',sys.argv[1] if len(sys.argv) > 1 else 'mapreduce-worker-failure.mp4')
