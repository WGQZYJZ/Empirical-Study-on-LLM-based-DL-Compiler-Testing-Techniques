import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
optimizer = torch.optim.Adadelta([x, y], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
for epoch in range(10):
    optimizer.zero_grad()
    loss = ((x ** 2) + (y ** 2))
    loss.backward()
    optimizer.step()
    print('Epoch {}, x: {}, y: {}'.format(epoch, x.item(), y.item()))