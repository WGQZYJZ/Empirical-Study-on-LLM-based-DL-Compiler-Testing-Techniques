import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.full_like(input, fill_value=4.0)
output = torch.full_like(input, fill_value=4.0, dtype=torch.int)