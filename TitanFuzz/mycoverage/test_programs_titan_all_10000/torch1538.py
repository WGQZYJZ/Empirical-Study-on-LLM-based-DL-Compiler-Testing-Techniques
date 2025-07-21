import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 3)
output_tensor = torch.Tensor.rot90(input_tensor, 1, dims=(1, 2))