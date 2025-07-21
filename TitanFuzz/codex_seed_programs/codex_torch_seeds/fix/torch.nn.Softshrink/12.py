'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(3, 3))
print(x)
import torch.nn as nn
x = Variable(torch.randn(3, 3))
y = nn.Softshrink(lambd=0.5)(x)
print(y)