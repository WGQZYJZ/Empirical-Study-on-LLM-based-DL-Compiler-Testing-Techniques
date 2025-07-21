import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
indices = torch.tensor([0, 2])
y = torch.take(x, indices)