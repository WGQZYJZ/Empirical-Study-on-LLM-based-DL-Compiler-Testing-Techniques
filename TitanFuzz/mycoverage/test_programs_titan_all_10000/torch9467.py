import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 4)
output_data = torch.Tensor.new_zeros(input_data, (2, 3, 4), dtype=None, device=None, requires_grad=False)