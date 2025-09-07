import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
out = torch.Tensor.is_meta(x)