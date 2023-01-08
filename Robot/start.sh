for session in $(screen -ls | grep -o '[0-9]\{3,\}.ServerTechV5')
    do
    	screen -r ServerTechV5 -p0 -X stuff "&9Server is restarting.\015"
    	screen -r ServerTechV5 -p0 -X stuff "stop\015" # Send "stop\r" to the server.
    done

counter=0
while [ $(screen -ls | grep -c '[0-9]\{3,\}.ServerTechV5') -ge 1 ]; do
	if [ $(( $counter % 10 )) -eq 0 ]; then
		echo 'A previous server is in use. Waiting for 10 seconds before starting server...'
	fi

	sleep 10
	counter=$((counter+1))
done

echo 'Starting server...'

	screen -dmS "ServerTechV5" sudo rfcomm watch hci0
	sleep 1
	while [ $(screen -ls | grep -c '[0-9]\{3,\}.ServerTechV5') -lt 1 ]; do
		echo 'Waiting for 5 seconds to start server...'
		sleep 5
		screen -dmS "ServerTechV5" sudo rfcomm watch hci0
	done

echo 'Server started.'