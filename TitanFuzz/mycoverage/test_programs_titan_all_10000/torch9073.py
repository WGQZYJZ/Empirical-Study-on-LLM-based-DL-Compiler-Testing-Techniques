import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 4)
output_data = torch.diag_embed(input_data, offset=0, dim1=(- 2), dim2=(- 1))