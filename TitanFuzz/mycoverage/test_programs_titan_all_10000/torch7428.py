import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 5)
b = torch.rand(5, 7)
c = torch.rand(7, 2)
torch.linalg.multi_dot([a, b, c])
torch.linalg.multi_dot([a, b, c], out=torch.zeros(3, 2))