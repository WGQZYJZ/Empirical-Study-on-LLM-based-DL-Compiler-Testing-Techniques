import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
input_tensor[(2, 2)] = float('nan')
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=True)