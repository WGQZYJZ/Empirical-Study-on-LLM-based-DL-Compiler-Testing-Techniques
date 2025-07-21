import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
other_tensor = torch.randn(3, 5)
result = torch.Tensor.maximum(input_tensor, other_tensor)