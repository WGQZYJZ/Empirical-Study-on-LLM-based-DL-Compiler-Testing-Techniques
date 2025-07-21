import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 5)
y = torch.vander(x, 3, True)