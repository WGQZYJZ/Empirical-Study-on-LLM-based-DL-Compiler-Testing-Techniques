import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 5)
torch.diag_embed(input, offset=0, dim1=(- 2), dim2=(- 1))