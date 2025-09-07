import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
y = torch.randn(3, 1)
res = torch.broadcast_tensors(x, y)