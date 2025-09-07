import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
mask = torch.ByteTensor([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]])
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, (- 1))