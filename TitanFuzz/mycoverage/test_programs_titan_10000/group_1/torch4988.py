import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 3)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 1], [1, 1, 1], [0, 0, 0]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)