import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.randn(2, 3)
result = torch.empty(2, 3, 3)
torch.dstack((x, y, z), out=result)