java -Dfile.encoding=Cp1252 -classpath /home/pi/Thesis/jason/libs/jason-2.6.jar:/home/pi/Thesis/jason/bin/ jason.infra.centralised.RunCentralisedMAS ${parameter}Test_${i}.mas2j & 

javaPid=$!

sleep 60s

/home/pi/jprofiler12/bin/jpenable --noinput --offline --pid=${javaPid} --config=/home/pi/Thesis/jprofiler_config.xml