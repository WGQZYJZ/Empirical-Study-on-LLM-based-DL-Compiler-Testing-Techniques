'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.psi\ntorch.special.psi(input, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(1, 1, requires_grad=True)
y = torch.special.psi(x)
print(y)
y.backward()
print(x.grad)