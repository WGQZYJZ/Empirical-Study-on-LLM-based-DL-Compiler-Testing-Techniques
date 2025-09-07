import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 3, 4, 5)
output = torch.broadcast_to(input, (2, 3, 4, 5))