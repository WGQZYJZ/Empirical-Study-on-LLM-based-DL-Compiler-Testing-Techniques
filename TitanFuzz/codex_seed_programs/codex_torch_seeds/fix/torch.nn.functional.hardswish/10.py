'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = torch.nn.functional.hardswish(x, inplace=False)
print('z = ', z)