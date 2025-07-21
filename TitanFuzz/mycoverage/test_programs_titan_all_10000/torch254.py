import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4, 5)
y = torch.Tensor.new_zeros(x, size=(4, 5))