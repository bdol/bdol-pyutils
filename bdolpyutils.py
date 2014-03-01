import sys

def progBar(t, N, length=20, barChar='=', headChar='>'):
  sys.stdout.write('\r')
  formatStr = '[%-'+str(length)+'s] %d%% (%d/%d)'
  sys.stdout.write(formatStr %
      (barChar*int(float(t)/float(N)*length)+headChar, 
        float(t)/float(N)*100, t, N))
  sys.stdout.flush()
