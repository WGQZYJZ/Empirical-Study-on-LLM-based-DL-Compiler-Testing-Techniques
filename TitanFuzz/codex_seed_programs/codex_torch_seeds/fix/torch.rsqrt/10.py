'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
x = Variable(torch.randn(1))
print('x: ', x)
y = torch.rsqrt(x)
print('y: ', y)
y = torch.rsqrt(x, out=x)
print('y: ', y)