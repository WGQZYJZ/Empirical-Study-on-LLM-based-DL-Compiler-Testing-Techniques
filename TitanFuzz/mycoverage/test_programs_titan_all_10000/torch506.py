import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
torch.nn.functional.elu_(x)