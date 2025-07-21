import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, 3, 3)
torch.nn.functional.leaky_relu_(x)