import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], requires_grad=True)
var = torch.var(x, dim=0)