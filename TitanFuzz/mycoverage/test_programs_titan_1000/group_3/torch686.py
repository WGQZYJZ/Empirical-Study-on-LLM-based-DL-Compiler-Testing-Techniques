import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.swapaxes(input_tensor, 0, 2)