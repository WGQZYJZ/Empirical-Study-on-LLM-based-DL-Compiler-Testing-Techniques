import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([0.3, 0.5, 0.7])
y = torch.special.erfc(x)