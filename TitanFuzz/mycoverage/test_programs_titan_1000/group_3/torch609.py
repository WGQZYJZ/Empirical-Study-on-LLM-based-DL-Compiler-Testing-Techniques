import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4, 5)
input_tensor[(1, 2, 3)] = float('nan')
input_tensor[(2, 1, 3)] = float('nan')
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5)
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5, dim=0)
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5, dim=1, keepdim=True)