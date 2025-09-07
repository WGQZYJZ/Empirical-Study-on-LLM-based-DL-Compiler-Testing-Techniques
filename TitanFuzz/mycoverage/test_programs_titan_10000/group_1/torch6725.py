import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(5)
y = torch.rand(5)
z = torch.minimum(x, y)