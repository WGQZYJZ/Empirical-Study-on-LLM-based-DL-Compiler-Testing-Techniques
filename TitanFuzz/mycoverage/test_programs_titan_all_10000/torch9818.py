import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
linear = torch.nn.Linear(in_features=2, out_features=1)
y = linear(x)
y.backward(torch.ones_like(y))