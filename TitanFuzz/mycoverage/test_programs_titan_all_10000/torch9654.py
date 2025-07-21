import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5, dtype=torch.float64)
pinverse = torch.pinverse(input)