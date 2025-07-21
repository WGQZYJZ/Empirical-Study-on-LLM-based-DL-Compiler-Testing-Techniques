import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.new_ones(input_tensor, (2, 2))