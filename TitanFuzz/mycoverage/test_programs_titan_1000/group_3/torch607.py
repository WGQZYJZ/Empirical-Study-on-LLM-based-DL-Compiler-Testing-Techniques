import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = torch.special.i1e(x)
y = torch.special.i1e(x, out=torch.empty(x.shape))