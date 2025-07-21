import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
result = torch.Tensor.bool(input_tensor, memory_format=torch.preserve_format)