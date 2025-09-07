import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 3)
mask = torch.tensor([[0, 0, 1], [0, 1, 0]])
source = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.masked_scatter_(input_tensor, mask, source)