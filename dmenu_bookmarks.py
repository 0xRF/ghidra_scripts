# Search Booksmarks With Dmenu
# @author 0xRF
# @category UI
# @keybinding Ctrl-B
# @menupath
# @toolbar

from subprocess import Popen, PIPE

p = Popen(
    ['rofi', '-dmenu', '-matching', 'fuzzy', '-async-pre-read', '0'],
    stdin=PIPE, stdout=PIPE
)

NOTE = currentProgram.bookmarkManager.getBookmarkType('Note')

for bookmark in currentProgram.bookmarkManager.getBookmarksIterator():
    if bookmark.getType().getTypeId() != NOTE.getTypeId():
        continue
    p.stdin.write("{} {}\n".format(bookmark.getId(), bookmark.getComment()))
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
