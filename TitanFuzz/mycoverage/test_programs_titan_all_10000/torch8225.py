import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 4)
y = torch.rand(4, 4)
torch.matmul(x, y)