import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3, 4)
output_tensor = torch.Tensor.arcsinh_(input_tensor)