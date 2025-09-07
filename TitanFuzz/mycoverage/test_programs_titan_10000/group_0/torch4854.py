import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([(- 1.0), 0.0, 1.0])
y = torch.atan(x)
y = torch.atan_(x)