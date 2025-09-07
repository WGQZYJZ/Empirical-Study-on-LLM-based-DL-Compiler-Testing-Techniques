import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.empty(5, 3)
output_tensor = torch.Tensor.new_ones(input_tensor, (2, 3), dtype=torch.float, device=None, requires_grad=True)