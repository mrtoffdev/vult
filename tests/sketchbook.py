
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
