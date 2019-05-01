nc -l 2222 | mplayer -fps 200 -demuxer h264es - &
nc -l 2223 | mplayer -fps 30 -demuxer h264es - &
ssh -t pi@10.10.10.10 'raspivid -t 0 -rot 270 -w 500 -h 500 -hf -fps 20 -o - | nc 10.10.10.1 2222' &
ssh -t pi@10.10.10.10 'ffmpeg -i /dev/video0 -f h264 -preset ultrafast pipe:1 | nc 192.168.0.118 2223' &
ssh -Y pi@10.10.10.10. 'cd Desktop/ && python key.py' 

