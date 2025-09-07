import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 3, 28, 28)
output_tensor = torch.Tensor.select(input_tensor, 1, 2)