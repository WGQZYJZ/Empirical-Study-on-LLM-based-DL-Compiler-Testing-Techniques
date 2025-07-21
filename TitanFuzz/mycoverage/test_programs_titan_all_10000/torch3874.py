import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5, 3, dtype=torch.float)
y = torch.randn(5, 2, dtype=torch.float)
torch.lstsq(x, y)