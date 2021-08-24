# Search Functions With Dmenu
# @author 0xRF
# @category UI
# @keybinding Ctrl-T
# @menupath
# @toolbar


from subprocess import Popen, PIPE

p = Popen(
    ['rofi', '-dmenu', '-async-pre-read', '0'],
    stdin=PIPE, stdout=PIPE
)

func = getFirstFunction()
while func is not None:
    p.stdin.write("{} {}\n".format(func.getName(), func.getEntryPoint()))
    func = getFunctionAfter(func)
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
    print('Failed to find function {}'.format(output))
