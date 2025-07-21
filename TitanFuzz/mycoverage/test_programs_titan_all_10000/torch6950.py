import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
cummin_tensor = torch.Tensor.cummin(input_tensor, dim=1)