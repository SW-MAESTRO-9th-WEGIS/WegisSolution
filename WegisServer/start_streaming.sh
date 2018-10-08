export LD_LIBRARY_PATH=/home/pi/{location of demo_app}//downloads/local/lib:$LD_LIBRARY_PATH
export AWS_ACCESS_KEY_ID={id}
export AWS_SECRET_ACCESS_KEY={key}
./kinesis_video_gstreamer_sample_app {kinesis stream name}
