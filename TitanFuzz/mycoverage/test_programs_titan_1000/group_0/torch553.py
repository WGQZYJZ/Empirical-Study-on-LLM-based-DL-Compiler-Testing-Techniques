import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = torch.optim.Adamax([x, y], lr=0.1)
for i in range(10):
    optimizer.zero_grad()
    z = ((x ** 2) + (y ** 2))
    z.backward()
    print(x.grad, y.grad)
    optimizer.step()