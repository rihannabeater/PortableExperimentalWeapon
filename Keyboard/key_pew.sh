nc -l 2222 | mplayer -fps 200 -demuxer h264es - &
ssh -t pi@10.10.10.10 'raspivid -t 0 -rot 270 -w 500 -h 500 -hf -fps 20 -o - | nc 10.10.10.5 2222' &
ssh -Y pi@10.10.10.10. 'cd Desktop/ && python key.py' 

