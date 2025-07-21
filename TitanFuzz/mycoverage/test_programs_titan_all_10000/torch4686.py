import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.new_zeros(input_tensor, (3, 4, 5))