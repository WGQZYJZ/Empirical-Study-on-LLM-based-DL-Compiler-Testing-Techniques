import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
result = torch.Tensor.nanmedian(input_tensor, dim=1)
result = torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=True)