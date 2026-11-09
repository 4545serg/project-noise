#include <3ds.h>
#include <stdio.h>

int main(void) {
    gfxInitDefault();
    PrintConsole top, bottom;
    consoleInit(GFX_TOP, &top);
    consoleInit(GFX_BOTTOM, &bottom);

    consoleSelect(&top);
    printf("\x1b[2;2HPROJECT NOISE");
    printf("\x1b[4;2HStage 1: build test OK");

    consoleSelect(&bottom);
    printf("\x1b[2;2HPress A to exit");

    while (aptMainLoop()) {
        hidScanInput();
        if (hidKeysDown() & KEY_A) break;
        gfxFlushBuffers();
        gfxSwapBuffers();
        gspWaitForVBlank();
    }

    gfxExit();
    return 0;
}
