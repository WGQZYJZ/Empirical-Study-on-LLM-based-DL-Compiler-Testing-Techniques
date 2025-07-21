import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4, 3)
output_tensor = torch.Tensor.diag_embed(input_tensor, offset=0, dim1=(- 2), dim2=(- 1))