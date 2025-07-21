import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(size=(3, 3))
output_tensor = torch.Tensor.mul(input_tensor, 2)