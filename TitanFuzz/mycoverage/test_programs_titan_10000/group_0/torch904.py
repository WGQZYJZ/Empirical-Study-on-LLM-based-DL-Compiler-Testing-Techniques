import torch
from torch import nn
from torch.autograd import Variable

a = torch.rand(3, 1)
b = torch.rand(3, 1)
c = torch.vstack([a, b])