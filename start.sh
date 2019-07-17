intexit() {
    # Kill all subprocesses (all processes in the current process group)
    kill -HUP -$$
}

hupexit() {
    # HUP'd (probably by intexit)
    echo
    echo "Interrupted"
    exit
}

trap hupexit HUP
trap intexit INT

x-terminal-emulator -e ./ngrok http 8000 &
NGROK_URL=`curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh` && echo $NGROK_URL && echo $NGROK_URL > temp && ./app.py &
./mitmdump -q --no-http2 -p 8084 -s ./main.py &

wait
