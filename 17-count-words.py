"""
Word counted
- remove punctuation, new lines, etc
- lower case all the words
- split into words
- count the words
- - loop through the words and use a dictionary to track the count
"""
from rich import print


lorem = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lobortis dui nec diam semper, tristique facilisis sapien laoreet. Aenean eget massa at mauris dictum gravida vel eu turpis. Pellentesque lobortis enim et lorem cursus faucibus. Proin ultricies ornare lacus. Phasellus pulvinar venenatis dui vel tempor. Donec euismod, lectus id congue varius, orci diam laoreet mi, in faucibus neque dolor eget lorem. Fusce et viverra tortor. Nunc rutrum nisl accumsan, venenatis leo eu, placerat libero.

Suspendisse eu gravida massa, vestibulum vulputate lorem. Sed in tempor lectus, nec tempor tortor. Pellentesque varius nisl a dolor viverra cursus. Morbi ex purus, semper id luctus eu, laoreet id elit. Morbi vitae nisl iaculis, ultrices ipsum in, suscipit enim. Maecenas tincidunt commodo vulputate. In in nulla quis ligula sodales finibus sit amet a ante. Phasellus accumsan laoreet justo, vel accumsan lectus sodales ullamcorper.

Etiam vitae ante dolor. Sed ullamcorper urna at ultricies dapibus. Curabitur eu sem rutrum, fermentum sapien vel, vehicula nunc. Donec non nisl eget est sodales pharetra. Quisque placerat ultrices nibh sed maximus. Vestibulum interdum massa ligula, id euismod tellus egestas et. Phasellus maximus tellus nec diam condimentum, nec accumsan eros consectetur. Pellentesque ultrices erat non tortor mollis, feugiat auctor elit iaculis. Morbi at rhoncus magna, condimentum pulvinar est. Ut gravida lacinia sem, vel dapibus leo euismod non. Praesent ac nulla hendrerit, viverra ante ac, ullamcorper justo. Nunc euismod semper tristique. Sed pulvinar a elit sed sagittis.

Curabitur ultrices auctor porta. Quisque sit amet justo vitae nisl porttitor ultrices quis et ipsum. Integer eleifend risus a mollis cursus. Vivamus vitae odio dapibus, egestas dui id, porta arcu. Praesent non nisl eu velit tristique pulvinar sagittis molestie arcu. Integer id ante vitae ante aliquet egestas eu eu turpis. Etiam fringilla metus sed odio volutpat malesuada. Etiam dignissim lectus ante, nec accumsan dui porta et. Praesent sagittis libero luctus, venenatis turpis vel, porta libero. Cras interdum purus id eros pulvinar viverra. Morbi turpis augue, ultrices quis est non, porttitor rhoncus sem. Pellentesque elementum ex in bibendum mattis. In semper efficitur erat, id ultricies ante venenatis sed. Mauris semper dignissim pharetra.

Vestibulum bibendum ex sed mauris dignissim, sed aliquam nunc rhoncus. Integer eu volutpat dolor, id eleifend tortor. Pellentesque feugiat scelerisque purus nec fermentum. Proin tincidunt convallis feugiat. Ut laoreet euismod arcu. Nulla lobortis augue nec sapien porta egestas. Suspendisse sed dictum ante, et scelerisque nibh. Fusce nec nibh vulputate, condimentum urna ut, viverra leo. Quisque ut nunc purus.
"""

lorem = lorem.replace(',', '')
lorem = lorem.replace('.', '')
lorem = lorem.replace('\n', ' ')
lorem = lorem.lower()
words = lorem.split(' ')

counts = {}
for word in words:
    if word == "": 
        continue

    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)