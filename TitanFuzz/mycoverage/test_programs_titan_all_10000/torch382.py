import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([0.5, 0.1, 0.3, 0.2])
a = torch.tensor([0.5, 0.1, 0.3, 0.2])
y = torch.special.gammaincc(x, a)