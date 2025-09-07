import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
cummin_tensor = torch.Tensor.cummin(input_tensor, dim=2)