import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([1, 2])
y = torch.atleast_2d(x)