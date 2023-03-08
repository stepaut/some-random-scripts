@Echo Off
SetLocal EnableDelayedExpansion
:: Расширение файлов для переименования
Set ext=mp3
:: Путь к папке с файлами
Set FPath=.

For /F "tokens=*" %%A In ('Dir "%FPath%\*.%ext%" /B /A-D') Do (
Call :RndGen
Ren "%FPath%\%%A" "!NM!.%ext%"
)
Pause && Exit

:RndGen
Set NM=
Set I=7
Set N=26
Set Charset=abcdefghijklmnopqrstuvwxyz
:RndGenLoop
Set /A R=%N%*%Random%/32768
Set NM=!Charset:~%R%,1!%NM%
Set /A I-=1
If %I% GTR 0 GoTo RndGenLoop