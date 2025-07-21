import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
output = torch.as_strided(input, (2, 3, 3), (12, 4, 1))
input = torch.randn(2, 3, 4)
output = torch.as_strided(input, (2, 3, 3), (12, 4, 1))