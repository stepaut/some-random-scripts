@echo off

SETLOCAL ENABLEDELAYEDEXPANSION

@echo TRIM

@set suff=_s.mp4

@for %%i in (*.mp4) do @(
@set f=%%~ni
echo !f!
ffmpeg -i %%i -an -vf setpts=0.00208*PTS %%~ni%suff%
)


@pause