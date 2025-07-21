import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.randn_like(input)
output = torch.randn_like(input, dtype=torch.float)
output = torch.rand_like(input)
output = torch.empty_like(input)
output = torch.full_like(input, fill_value=4)
output = torch.zeros_like(input)
output = torch.ones_like(input)