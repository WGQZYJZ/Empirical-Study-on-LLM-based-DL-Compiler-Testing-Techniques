import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10)
output = torch.kaiser_window(10, periodic=True, beta=12.0)