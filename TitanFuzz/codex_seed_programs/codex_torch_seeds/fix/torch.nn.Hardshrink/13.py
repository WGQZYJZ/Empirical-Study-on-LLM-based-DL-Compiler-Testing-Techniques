'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
print(torch.nn.Hardshrink(lambd=0.5)(x))