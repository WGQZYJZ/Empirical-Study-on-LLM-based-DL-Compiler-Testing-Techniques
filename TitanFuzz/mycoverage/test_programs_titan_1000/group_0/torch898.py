import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
a_ge = torch.ge(a, a)
b = torch.randn(4, 4)
b_ge = torch.ge(a, b)