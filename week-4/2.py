from src import Stack

s = Stack()

s.push('w').push('e')

print('Size:', s.size(), "- Empty:", s.isEmpty(),
      "- First Value:", s.peek(), "- First Value popped:", s.pop().data, s.peek())
