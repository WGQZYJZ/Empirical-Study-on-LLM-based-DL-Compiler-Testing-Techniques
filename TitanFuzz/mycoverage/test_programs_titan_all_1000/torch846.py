import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
with torch.set_grad_enabled(False):
    print(torch.is_grad_enabled())
with torch.set_grad_enabled(True):
    print(torch.is_grad_enabled())
with torch.no_grad():
    print(torch.is_grad_enabled())