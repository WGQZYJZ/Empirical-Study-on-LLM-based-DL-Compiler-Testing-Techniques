import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
diagonal = torch.diag_embed(input)
diagonal = torch.diag_embed(input, offset=1)
diagonal = torch.diag_embed(input, offset=(- 1))
diagonal = torch.diag_embed(input, dim1=0, dim2=1)
diagonal = torch.diag_embed(input, dim1=0, dim2=2)
diagonal = torch.diag_embed(input, dim1=1, dim2=2)
diagonal = torch.diag_embed(input, dim1=0, dim2=1, offset=1)
diagonal = torch.diag_embed(input, dim1=0, dim2=1, offset=(- 1))