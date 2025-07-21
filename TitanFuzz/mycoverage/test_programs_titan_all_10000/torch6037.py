import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, dtype=torch.float64)
y = torch.special.erfcx(x)