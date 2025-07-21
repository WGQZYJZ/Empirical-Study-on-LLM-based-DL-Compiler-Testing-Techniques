import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([float('inf'), float('-inf'), float('nan'), float('1')])
output = torch.isposinf(input)