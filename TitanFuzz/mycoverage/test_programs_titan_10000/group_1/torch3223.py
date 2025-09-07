import torch
from torch import nn
from torch.autograd import Variable

if True:
    x = torch.randn(2, 3, 3)
    print(x)
    print(torch.is_warn_always_enabled())