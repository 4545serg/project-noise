import struct, zlib, wave

def png(path, w, h, rgb):
    raw = b''.join(b'\x00' + bytes(rgb) * w for _ in range(h))
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    data = (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw))
            + chunk(b'IEND', b''))
    open(path, 'wb').write(data)

png('icon.png', 48, 48, (29, 185, 84))
png('banner.png', 256, 128, (18, 18, 18))
w = wave.open('silence.wav', 'wb')
w.setnchannels(2); w.setsampwidth(2); w.setframerate(22050)
w.writeframes(b'\x00\x00\x00\x00' * 22050)
w.close()
