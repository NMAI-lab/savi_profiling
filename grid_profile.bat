START "" "C:\Program Files\Java\jre1.8.0_291\bin\java.exe" -Dfile.encoding=Cp1252 -classpath "D:\Local Documents\Github\jasonMobileAgent\lib\aima-core.jar";"D:\Local Documents\Github\jasonMobileAgent\bin\classes";"D:\Local Documents\Github\jasonMobileAgent";"D:\Local Documents\Utilities\jason-2.6.2\libs\jason-2.6.2.jar" jason.infra.centralised.RunCentralisedMAS "D:\Local Documents\Github\jasonMobileAgent\jasonMobileAgent.mas2j"

for /F "TOKENS=1,2,*" %%a in ('tasklist /FI "IMAGENAME eq java.exe"') do set MyPID=%%b

timeout /t 10 /nobreak > NUL

"C:\Program Files\jprofiler12\bin\jpenable" --noinput --offline --pid=%MyPID% --config="D:\Local Documents\Github\savi_profiling\jprofiler_config_deliberate.xml"

timeout /t 10 /nobreak > NUL

taskkill /F /PID %MyPID%

