import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(2, 2, requires_grad=True)
with torch.no_grad():
    print(a.requires_grad)
    print(torch.is_grad_enabled())