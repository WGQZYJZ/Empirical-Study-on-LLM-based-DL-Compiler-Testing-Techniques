import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
value = 3.1415926
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)