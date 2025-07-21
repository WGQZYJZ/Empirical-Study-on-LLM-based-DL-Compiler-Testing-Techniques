import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
result_tensor = torch.Tensor.any(input_tensor, dim=None, keepdim=False)