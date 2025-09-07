import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(2, 3, 4)
y = torch.rand_like(x)