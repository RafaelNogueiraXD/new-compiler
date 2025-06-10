.386
.model flat, stdcall
option casemap:none

include windows.inc
include user32.inc
include kernel32.inc

includelib user32.lib
includelib kernel32.lib

.data
    msgTitle db "Mensagem", 0
    msgText  db "Olá, Mundo!", 0

.code
start:
    ; Chama MessageBoxA (NULL, msgText, msgTitle, MB_OK)
    invoke MessageBoxA, NULL, addr msgText, addr msgTitle, MB_OK

    ; Encerra o programa
    invoke ExitProcess, 0
end start
