import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 4)
v = torch.rand(4)
y = torch.mv(x, v)