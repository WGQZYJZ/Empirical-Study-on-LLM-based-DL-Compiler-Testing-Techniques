import torch
from torch import nn
from torch.autograd import Variable
y = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
result = torch.trapz(y)
result = torch.trapz(y, dx=2)
result = torch.trapz(y, dx=2, dim=0)
result = torch.trapz(y, dx=2, dim=1)