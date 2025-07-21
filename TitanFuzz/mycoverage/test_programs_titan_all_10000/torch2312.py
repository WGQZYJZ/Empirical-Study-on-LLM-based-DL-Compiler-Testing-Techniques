import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3, 4)
output_tensor = torch.Tensor.transpose_(input_tensor, 1, 2)