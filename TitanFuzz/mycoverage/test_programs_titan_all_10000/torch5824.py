import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[3, 4, 2], [5, 1, 7]])
y = torch.sort(x, descending=True)
z = torch.sort(x, descending=True, dim=1)
a = torch.sort(x, descending=False, dim=1)