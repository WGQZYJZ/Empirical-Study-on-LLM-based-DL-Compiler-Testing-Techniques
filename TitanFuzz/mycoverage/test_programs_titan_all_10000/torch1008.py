import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.resize_as_(input_tensor, tensor)