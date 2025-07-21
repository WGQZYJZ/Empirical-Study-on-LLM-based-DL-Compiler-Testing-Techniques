import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
output = torch.cumsum(input, dim=1)
output1 = torch.cumsum(input, dim=1, out=torch.empty(input.size()))
output2 = torch.cumsum(input, dim=1, dtype=torch.float64)