import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.le(input, 0)
output_with_out = torch.empty(4, 4)
torch.le(input, 0, out=output_with_out)