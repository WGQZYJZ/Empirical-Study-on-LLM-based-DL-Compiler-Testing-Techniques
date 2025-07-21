import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 10, dtype=torch.float64)
y = torch.special.i1e(x)