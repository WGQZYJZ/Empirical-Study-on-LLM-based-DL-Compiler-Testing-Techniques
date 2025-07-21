import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 11, dtype=torch.float32)
y = torch.special.i0(x)