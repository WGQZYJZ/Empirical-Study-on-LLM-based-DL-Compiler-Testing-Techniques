import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 1, 3, 1, 1)
output = torch.squeeze(input)
output = torch.squeeze(input, dim=0)
output = torch.squeeze(input, dim=2)
output = torch.squeeze(input, dim=4)
output = torch.squeeze(input, dim=1)