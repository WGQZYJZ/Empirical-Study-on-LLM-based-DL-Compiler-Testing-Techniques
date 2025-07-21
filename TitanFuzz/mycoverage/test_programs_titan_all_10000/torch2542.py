import torch
from torch import nn
from torch.autograd import Variable
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
torch.cartesian_prod(a, b)
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = torch.tensor([7, 8, 9])
torch.cartesian_prod(a, b, c)