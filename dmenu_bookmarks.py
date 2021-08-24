# Search Booksmarks With Dmenu
# @author 0xRF
# @category UI
# @keybinding Ctrl-B
# @menupath
# @toolbar

from subprocess import Popen, PIPE

p = Popen(
    ['rofi', '-dmenu', '-async-pre-read', '0'],
    stdin=PIPE, stdout=PIPE
)


for bookmark in currentProgram.bookmarkManager.getBookmarksIterator():
    p.stdin.write("{} {} {}\n".format(bookmark.getId(), bookmark.getComment(), bookmark.getTypeString()))
    if p.poll() is not None:
        break

if p.poll() is None:
    p.stdin.close()
    p.wait()
output = p.stdout.readline().rstrip('\n').split()

try:
    bookmark = currentProgram.bookmarkManager.getBookmark(int(output[0]))
    print('Bookmark ID: {}'.format(int(output[0])))
    goTo(bookmark.getAddress())
except:
    print('Failed to find bookmark {}'.format(output))
