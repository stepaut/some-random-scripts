SETLOCAL ENABLEDELAYEDEXPANSION
@echo TRIM

@set suff=_FF.mp4

@for %%i in (*.mp4) do @(
@set f=%%~ni
echo !f!
ffmpeg -ss 10 -i %%i -c copy %%~ni%suff%
)


@pause