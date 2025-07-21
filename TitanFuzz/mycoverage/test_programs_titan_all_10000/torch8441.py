import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
output = torch.diag_embed(input)
output = torch.diag_embed(input, offset=1)
output = torch.diag_embed(input, offset=1, dim1=1, dim2=2)