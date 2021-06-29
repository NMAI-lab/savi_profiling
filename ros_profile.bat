for /F "TOKENS=1,2,*" %%a in ('tasklist /FI "IMAGENAME eq java.exe"') do set MyPID=%%b

"C:\Program Files\jprofiler12\bin\jpenable" --noinput --offline --pid=%MyPID% --config="D:\Local Documents\Github\savi_profiling\jprofiler_config_ros.xml"

timeout /t 30 /nobreak > NUL

taskkill /F /PID %MyPID%
