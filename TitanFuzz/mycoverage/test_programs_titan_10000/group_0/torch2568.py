import torch
from torch import nn
from torch.autograd import Variable

a = torch.tensor([1, 2, 3, 4, 5])
b = torch.tensor([1, 2, 3, 4, 5])
torch.vdot(a, b)