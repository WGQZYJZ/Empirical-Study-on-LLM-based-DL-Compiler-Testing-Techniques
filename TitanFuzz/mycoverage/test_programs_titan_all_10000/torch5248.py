import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
mask = torch.tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]], dtype=torch.bool)
source = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
torch.Tensor.masked_scatter_(input_tensor, mask, source)