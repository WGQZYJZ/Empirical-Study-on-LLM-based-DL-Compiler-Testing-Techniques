import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
linear = torch.nn.Linear(2, 1)
y = linear(x)
y.backward(torch.ones_like(y))