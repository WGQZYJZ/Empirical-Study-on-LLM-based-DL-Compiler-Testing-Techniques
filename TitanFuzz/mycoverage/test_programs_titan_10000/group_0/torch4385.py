import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.contiguous(input_tensor, memory_format=torch.contiguous_format)