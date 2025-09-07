import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
output = torch.diag_embed(input, offset=0, dim1=(- 2), dim2=(- 1))
output = torch.diag_embed(input, offset=0, dim1=0, dim2=2)