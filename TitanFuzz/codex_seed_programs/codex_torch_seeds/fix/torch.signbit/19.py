'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([(- 1), 0, 1]))
y = torch.signbit(x)
print('y = ', y)