import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 1, 1, 1, 1])
torch.le(x, y)
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 1, 1, 1, 1])
torch.lt(x, y)
x = torch.tensor([1, 2, 3, 4, 5])