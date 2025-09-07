import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(2, 3)
value = 2
output_tensor = torch.Tensor.multiply(input_tensor, value)