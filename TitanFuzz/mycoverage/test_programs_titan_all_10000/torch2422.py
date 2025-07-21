import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 1)
y = torch.broadcast_to(x, (3, 3))