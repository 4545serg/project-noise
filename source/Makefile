ifeq ($(strip $(DEVKITARM)),)
$(error DEVKITARM is not set)
endif

TARGET  := PROJECT_NOISE
TOOLS   := $(DEVKITPRO)/tools/bin
CC      := $(DEVKITARM)/bin/arm-none-eabi-gcc
ARCH    := -march=armv6k -mtune=mpcore -mfloat-abi=hard -mtp=soft
CFLAGS  := -g -Wall -O2 -mword-relocations -ffunction-sections $(ARCH) -D__3DS__ -Isource -I$(DEVKITPRO)/libctru/include
LDFLAGS := -specs=3dsx.specs -g $(ARCH) -L$(DEVKITPRO)/libctru/lib
LIBS    := -lctru -lm
SRCS    := $(wildcard source/*.c)
OBJS    := $(SRCS:.c=.o)

.RECIPEPREFIX := >

all: $(TARGET).3dsx

%.o: %.c
> $(CC) $(CFLAGS) -c $< -o $@

$(TARGET).elf: $(OBJS)
> $(CC) $(LDFLAGS) $(OBJS) $(LIBS) -o $@

$(TARGET).smdh: icon.png
> $(TOOLS)/smdhtool --create "PROJECT NOISE" "Native MP3 player" "PROJECT NOISE" icon.png $@

$(TARGET).3dsx: $(TARGET).elf $(TARGET).smdh
> $(TOOLS)/3dsxtool $(TARGET).elf $@ --smdh=$(TARGET).smdh

clean:
> rm -f source/*.o *.elf *.3dsx *.smdh *.cia *.bnr
