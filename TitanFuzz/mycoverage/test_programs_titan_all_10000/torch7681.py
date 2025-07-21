import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 5)
y = torch.triu(x)
y1 = torch.triu(x, diagonal=1)
y2 = torch.triu(x, diagonal=2)