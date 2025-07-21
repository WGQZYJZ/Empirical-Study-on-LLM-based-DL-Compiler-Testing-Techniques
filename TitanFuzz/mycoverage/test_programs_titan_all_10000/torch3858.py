import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace(0, 1, 5)
y = torch.tensor([0, 1, 2, 3, 4])
result = torch.trapz(y, x)