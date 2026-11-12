# Ship Log contest entry

`main.py` copies the bytes of `art.jpg` to `/output/entry.png`. The copy is exact: the program does not decode or re-encode the image. The output filename ends in `.png` because the contest requires that path; the file contents stay the original JPEG bytes.

The program uses only the Python standard library (`pathlib` and `shutil`). It has no third-party dependencies and does not use the network. Running it twice writes the same bytes.

## Run

```bash
python main.py
```

The program creates `/output` when that directory is missing, then replaces `/output/entry.png` with a bit-for-bit copy of `art.jpg`.
