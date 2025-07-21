import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.complex(a, b)