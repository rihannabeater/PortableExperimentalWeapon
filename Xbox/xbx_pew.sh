nc -l 2222 | mplayer -fps 200 -demuxer h264es - &
ssh -t pi@197.164.1.236 'raspivid -t 0 -rot 270 -w 500 -h 500 -hf -fps 20 -o - | nc 197.164.1.210 2222' &
ssh -Y pi@197.164.1.236 'cd Desktop/ && python xbx.py' 

