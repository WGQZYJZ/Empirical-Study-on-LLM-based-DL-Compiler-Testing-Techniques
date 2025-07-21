import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
torch.masked_select(x, (x > 0.5))