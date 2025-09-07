import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 5)
result = torch.Tensor.argmin(input_tensor, dim=1, keepdim=True)