import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
optimizer = torch.optim.RMSprop([x], lr=0.01)
for i in range(3):
    optimizer.zero_grad()
    y = (x ** 2)
    loss = y.sum()
    loss.backward()
    optimizer.step()
    print('x: {}, loss: {}'.format(x, loss.item()))