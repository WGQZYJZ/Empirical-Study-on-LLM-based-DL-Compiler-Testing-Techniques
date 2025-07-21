import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, 4)
y = torch.reshape(x, ((- 1), 3, 4))
y = torch.reshape(x, (2, 3, 4))
y = torch.reshape(x, (1, 6, 4))
y = torch.reshape(x, (1, 3, 8))
y = torch.reshape(x, (1, 24))