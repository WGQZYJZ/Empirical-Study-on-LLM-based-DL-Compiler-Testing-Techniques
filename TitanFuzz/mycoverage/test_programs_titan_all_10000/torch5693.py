import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.roll(x, 1, dims=1)
y = torch.roll(x, (- 1), dims=1)