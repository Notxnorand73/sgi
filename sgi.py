import sys
import json

def compile(jsonlist):
    '''
    int -> int
    'stop' -> 256
    '''
    binary = []
    for i in jsonlist:
        if isinstance(i, int):
            binary.append(i)
        elif i == 'stop':
            binary.append(256)
    '''turn integers into signed 2 bytes represented as a string'''
    compiled = []
    for i in binary:
        if i == 256:
            compiled.append('00000001')
            compiled.append('00000000')
        else:
            if i < 0:
                i = (1 << 16) + i
            compiled.append(format(i, '016b'))
    return ''.join(str(b) for b in compiled)

def decompile(binary):
    '''
    int -> int
    'stop' -> 256
    '''
    jsonlist = []
    for i in range(0, len(binary), 16):
        chunk = binary[i:i+16]
        if chunk == '0000000100000000':
            jsonlist.append('stop')
        else:
            value = int(chunk, 2)
            if value >= (1 << 15):
                value -= (1 << 16)
            jsonlist.append(value)
    return jsonlist

if __name__ == "__main__":
    if len(sys.argv) > 3:
        filename = sys.argv[1]
        tag = sys.argv[2]
        input = sys.argv[3]
        if tag == "compile":
            try:
                with open(filename, 'w') as f:
                    f.write(compile(json.loads(input)))
                print('Compiled successfully!')
            except Exception as e:
                print(f"Error compiling:\n   {e}")
        elif tag == "decompile":
            try:
                with open(filename, 'w') as f:
                    f.write(json.dumps(decompile(input)))
                print('Decompiled successfully!')
            except Exception as e:
                print(f"Error decompiling:\n   {e}")
        else:
            print("Tag must be 'compile' or 'decompile'")
    else:
        print("requires 3 arguments: filename, tag (compile/decompile), and input")
