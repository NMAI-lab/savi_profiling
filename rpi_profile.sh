ps -a
javaPid=$!
/home/pi/jprofiler12/bin/jpenable --noinput --offline --pid=${javaPid} --config=/home/pi/savi_profiling/savi_profiling/jprofiler_config_ros.xml