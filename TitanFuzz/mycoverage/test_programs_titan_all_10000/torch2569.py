import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
output_data = torch.Tensor.new_empty(input_data, size=(3, 4), dtype=torch.int64, device=None, requires_grad=False)