if ! screen -list | grep -q ServerTechV5; then
	echo "$(date) $(ls -1 | wc -l):" >> /home/isri/Desktop/python/GestionDeProjets_Upjv_Gr2/Robot/MCServerRestartLog.txt 2>&1
	cd /home/isri/Desktop/python/GestionDeProjets_Upjv_Gr2/Robot
    "/home/isri/Desktop/python/GestionDeProjets_Upjv_Gr2/Robot/start.sh" | sed 's/^/  /' >> /home/isri/Desktop/python/GestionDeProjets_Upjv_Gr2/Robot/MCServerRestartLog.txt 2>&1
fi
