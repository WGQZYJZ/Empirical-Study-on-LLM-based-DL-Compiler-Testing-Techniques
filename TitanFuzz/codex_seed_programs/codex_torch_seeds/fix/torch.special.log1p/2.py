'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.log1p\ntorch.special.log1p(input, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = torch.randn(1)
x = Variable(x, requires_grad=True)
y = torch.special.log1p(x)
y.backward()
print(x)
print(y)
print(x.grad)