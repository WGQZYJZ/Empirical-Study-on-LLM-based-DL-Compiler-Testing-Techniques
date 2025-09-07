import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
with torch.no_grad():
    print('torch.is_grad_enabled() = ', torch.is_grad_enabled())
    y = torch.randn(1)
    print('y = ', y)