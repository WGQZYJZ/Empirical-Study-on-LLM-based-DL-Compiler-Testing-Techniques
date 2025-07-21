import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.resize_as_(input_tensor, output_tensor)