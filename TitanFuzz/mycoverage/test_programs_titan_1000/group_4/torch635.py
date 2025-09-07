import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), requires_grad=True)
y = torch.special.psi(x)