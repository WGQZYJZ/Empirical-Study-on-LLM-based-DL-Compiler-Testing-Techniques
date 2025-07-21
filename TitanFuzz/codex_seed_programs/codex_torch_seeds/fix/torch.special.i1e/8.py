'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i1e\ntorch.special.i1e(input, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
print('x:', x)
y = torch.special.i1e(x)
print('y:', y)