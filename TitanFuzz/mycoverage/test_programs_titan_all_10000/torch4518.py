import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.randn(2, 3)
torch.Tensor.addcmul(x, y, z, value=1)