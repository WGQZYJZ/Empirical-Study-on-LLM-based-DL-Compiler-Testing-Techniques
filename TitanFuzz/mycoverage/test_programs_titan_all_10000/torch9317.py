import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
result = torch.Tensor.maximum(input_tensor, other)