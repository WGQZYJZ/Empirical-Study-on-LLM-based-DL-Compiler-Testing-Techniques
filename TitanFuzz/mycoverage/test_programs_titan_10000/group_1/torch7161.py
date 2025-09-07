import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(3, 3, requires_grad=True)
output = torch.Tensor.bool(input_tensor)