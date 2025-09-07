import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor(1.0)
y = torch.tensor(2.0)
z = torch.divide(x, y)