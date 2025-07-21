import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
result_tensor = torch.Tensor.nanquantile(input_tensor, 0.5, dim=None, keepdim=False)