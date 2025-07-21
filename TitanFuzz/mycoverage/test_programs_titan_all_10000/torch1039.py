import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace((- 2), 2, 100)
y = torch.nn.functional.leaky_relu_(x)