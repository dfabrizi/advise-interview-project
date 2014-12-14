@echo off
set "VIRTUAL_ENV=C:\Users\wildcat\Documents\Advise_Project\interview_site"

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
    if not defined PROMPT (
        set "PROMPT=$P$G"
    )
	set "_OLD_VIRTUAL_PROMPT=%PROMPT%"	
)
set "PROMPT=(interview_site) %PROMPT%"

if not defined _OLD_VIRTUAL_PYTHONHOME (
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
)
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
) else (
    set "_OLD_VIRTUAL_PATH=%PATH%"
)
set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

:END
