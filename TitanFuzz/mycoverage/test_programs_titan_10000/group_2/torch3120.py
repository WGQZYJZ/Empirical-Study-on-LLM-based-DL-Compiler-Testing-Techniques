import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3)
size = (3, 2)
output_tensor = torch.Tensor.new_empty(input_tensor, size, dtype=None, device=None, requires_grad=False)