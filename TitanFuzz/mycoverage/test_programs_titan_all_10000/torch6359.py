import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 5)
output_tensor = torch.Tensor.floor_divide_(input_tensor, 2)