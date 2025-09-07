import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = 0.5
output_tensor = torch.Tensor.greater(input_tensor, other)