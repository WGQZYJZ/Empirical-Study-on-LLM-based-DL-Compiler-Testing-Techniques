import torch
from torch import nn
from torch.autograd import Variable
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.trapezoid(y)