import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
source = torch.rand(4)
torch.Tensor.masked_scatter_(input_tensor, mask, source)