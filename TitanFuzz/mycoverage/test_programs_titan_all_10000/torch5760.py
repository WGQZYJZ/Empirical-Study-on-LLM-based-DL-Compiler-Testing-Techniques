import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 3)
output = torch.full_like(input, fill_value=1)