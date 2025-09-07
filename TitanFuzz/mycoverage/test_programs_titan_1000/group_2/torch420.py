import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 1, 3)
squeeze_tensor = torch.Tensor.squeeze_(input_tensor, dim=2)
squeeze_tensor = torch.Tensor.squeeze_(input_tensor)