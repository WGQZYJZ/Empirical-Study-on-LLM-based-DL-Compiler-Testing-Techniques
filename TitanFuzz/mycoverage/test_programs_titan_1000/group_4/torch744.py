import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
output_tensor = torch.Tensor.new_empty(input_tensor, (3, 5))