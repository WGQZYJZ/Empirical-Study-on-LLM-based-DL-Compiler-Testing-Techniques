import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
dimension = 0
start = 2
length = 2
output_tensor = torch.Tensor.narrow_copy(input_tensor, dimension, start, length)