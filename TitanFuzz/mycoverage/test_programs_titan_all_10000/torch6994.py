import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0]])
value = 10
torch.Tensor.masked_fill_(input_tensor, mask, value)