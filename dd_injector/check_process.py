import subprocess

class Service():
    def __init__(self, process):
        self.process = process

    def status(self):
        p = subprocess.Popen(["ps", "ax"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        sout = str(out)
        if (self.process in sout.lower()):
            return 1
        else:
            return 0
