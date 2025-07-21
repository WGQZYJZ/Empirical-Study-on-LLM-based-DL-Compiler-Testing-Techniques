'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ne\ntorch.ne(input, other, *, out=None)\n'
import torch
from torch.autograd import Variable
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = Variable(torch.Tensor([[1, 2], [3, 4]]))
y = Variable(torch.Tensor([[5, 6], [7, 8]]))
print('Task 3: Call the API torch.ne')
print(torch.ne(x, y))
print(torch.ne(x, y).numpy())