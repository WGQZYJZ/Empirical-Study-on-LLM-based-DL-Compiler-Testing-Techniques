import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.new_empty(input_tensor, (2, 3, 4), dtype=torch.float32, device=None, requires_grad=False)