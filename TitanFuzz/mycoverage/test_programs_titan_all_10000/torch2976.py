import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 4)
y = torch.rand(4, 4)
z = torch.rand(4, 4)
output = torch.lerp(x, y, z)