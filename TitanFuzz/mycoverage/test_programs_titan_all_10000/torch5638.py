import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
is_quantized = torch.Tensor.is_quantized(input_tensor)