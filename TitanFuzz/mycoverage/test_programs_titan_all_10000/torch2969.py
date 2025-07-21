import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 2, 3, float('inf'), float('-inf'), float('nan')])
output = torch.isposinf(input)