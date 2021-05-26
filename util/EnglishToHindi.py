from englisttohindi.englisttohindi import EngtoHindi

def convert(message):
    res = EngtoHindi(message)
    return res.convert


if __name__=='__main__':
    print(convert("Hello , I am student"))