import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 1, 3, 1)
output = torch.broadcast_to(input, (4, 3, 3, 3))