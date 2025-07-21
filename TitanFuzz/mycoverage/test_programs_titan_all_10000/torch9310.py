import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 6)
result = torch.Tensor.dsplit(x, 2)
result = torch.Tensor.dsplit(x, [2, 3])