import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3)
linear_model = torch.nn.Linear(3, 1)
y = linear_model(x)