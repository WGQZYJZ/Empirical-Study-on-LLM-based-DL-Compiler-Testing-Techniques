import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10000, 1)
y = torch.rand(10000, 1)
torch.initial_seed()
z = (x + y)