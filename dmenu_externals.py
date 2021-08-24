# Search External Functions With Dmenu
# @author 0xRF
# @category UI
# @keybinding Ctrl-Y
# @menupath
# @toolbar


from subprocess import Popen, PIPE

p = Popen(
    ['rofi', '-dmenu', '-matching', 'fuzzy', '-async-pre-read', '0'],
    stdin=PIPE, stdout=PIPE
)

for extSym in currentProgram.getSymbolTable().getExternalSymbols():
    p.stdin.write("{} {}\n".format(extSym.getName(), extSym.getAddress()))
    if p.poll() is not None:
        break

if p.poll() is None:
    p.stdin.close()
    p.wait()

output = p.stdout.readline().rstrip('\n')

try:
    address = currentProgram.addressFactory.getAddress(output.split()[1])
    goTo(address)
except:
    print('Failed to find {}'.format(output))
