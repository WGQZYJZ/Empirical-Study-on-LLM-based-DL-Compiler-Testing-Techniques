import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
output_tensor = torch.Tensor.new_empty(input_tensor, (4, 3))