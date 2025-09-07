import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3)
output = torch.broadcast_to(input, (4, 2, 3))