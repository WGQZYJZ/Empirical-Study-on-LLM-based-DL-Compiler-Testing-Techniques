import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.ge(x, y)
torch.ge(x, y, out=z)