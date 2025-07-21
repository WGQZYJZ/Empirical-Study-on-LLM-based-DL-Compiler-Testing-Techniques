import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10)
result = torch.Tensor.log1p_(input_tensor)