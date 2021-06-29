@echo off

CD "D:\Local Documents\Github\savi_profiling\results\gridSynched\"
for /L %%D IN (0, 1, 37) DO (

	"C:\Program Files\jprofiler12\bin\jpexport.exe" "Snapshot.%%D.jps" CallTree "snapshot_%%D.xml"

)