import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(1, 10, (3, 4))
cummin = torch.cummin(input, dim=1)