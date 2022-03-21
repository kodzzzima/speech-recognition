import json
import re

from vosk import Model, KaldiRecognizer


def recognition(wave_file):
    model = Model("vosk-model-small-ru-0.22")

    rcgn_fr = wave_file.getframerate() * wave_file.getnchannels()
    rec = KaldiRecognizer(model, rcgn_fr)
    result = ''
    last_n = False
    read_block_size = wave_file.getnframes()
    while True:
        data = wave_file.readframes(read_block_size)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())

            if res['text'] != '':
                result += f" {res['text']}"
                if read_block_size < 200000:
                    print(res['text'] + " \n")

                last_n = False
            elif not last_n:
                result += '\n'
                last_n = True

    res = json.loads(rec.FinalResult())
    result += f" {res['text']}"

    return '\n'.join(line.strip() for line in re.findall(r'.{1,150}(?:\s+|$)', result))
