import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 4, 5)
output = torch.flatten(input)
output = torch.flatten(input, start_dim=1)
output = torch.flatten(input, start_dim=1, end_dim=2)