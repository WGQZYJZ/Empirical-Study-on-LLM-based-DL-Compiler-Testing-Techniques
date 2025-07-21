import torch
from torch import nn
from torch.autograd import Variable
y = torch.tensor([1.0, 2.0, 3.0, 4.0])
result = torch.trapz(y)