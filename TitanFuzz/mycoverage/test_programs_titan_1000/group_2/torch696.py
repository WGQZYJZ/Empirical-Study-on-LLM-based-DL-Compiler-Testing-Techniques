import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
output_data = torch.Tensor.new_full(input_data, 3, fill_value=1, dtype=None, device=None, requires_grad=False)