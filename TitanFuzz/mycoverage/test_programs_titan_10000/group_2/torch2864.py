import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(1, 2, 3)
result = torch.Tensor.neg(input_tensor)