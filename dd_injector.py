import dd_injector
import os

def main():
    sender = dd_injector.DD()
    conf = dd_injector.Conf()
    access_log_check(sender, conf)
    process_check(sender, conf)
    s3_log_check(sender, conf)
 
def access_log_check(s,c):
    access_log = c._read('access_log')['location']
    if os.path.isfile(access_log):
        filestats = dd_injector.Stats(access_log)
        size = filestats.size()
        age = filestats.age()
        s.inject('access.log.size',size)
        s.inject('access.log.age',age)
    else:
        print "{} does not exist.. skipping access_log check".format(access_log)

def process_check(s,c): 
    procs = {}   
    for k, v in c._read('proc_check').iteritems():
        procs[k] = dd_injector.Service(v)
    for k, v in procs.iteritems():
        s.inject(k+'.status',v.status())

def s3_log_check(s,c):
    s3_log = {}
    for k,v in c._read('s3_log').iteritems():
        s3_log[k] = v
        c = 0
        if os.path.isdir(v):
            for fn in os.listdir(v):
                if fn.endswith(".log"):
                    c = c+1
                    filestats = dd_injector.Stats(os.path.join(v,fn))
                    size = filestats.size()
                    age = filestats.age_minutes()
                    s.inject(k+'.'+str(c)+'.log.size',size)
                    s.inject(k+'.'+str(c)+'.log.age',age)
        else:
            print "{} does not exist.. skipping {} log check".format(v,k)

if __name__ == '__main__':
    main()
