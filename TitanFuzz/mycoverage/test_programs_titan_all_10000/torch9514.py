import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, requires_grad=True)
y = torch.randn(2, 3, requires_grad=True)
torch._assert((x.shape == y.shape), 'Shape mismatch')