
'''
Todo:
1. find bindings for ffmpeg-cli commands in ffmpeg-python library
2. include support for off-standard codec + format combinations (e.g. h265 enc in .mov)
3. bind textual frontend to vult_core ffmpeg operations
        A. CRF auto adjustment in backend + supporting sliders / group radio button
        B. Resolution auto adjustment to occupy only frame required space instead of
                container required space
'''
def prefix():
        input   = "./test"
        output: str

        if input.startswith("./"):
                output  = input.lstrip('./')
                print("prefix: ./")
                print(f'output: {output}')
        else:
                print("prefix not found")

if __name__ == '__main__':
        prefix()
