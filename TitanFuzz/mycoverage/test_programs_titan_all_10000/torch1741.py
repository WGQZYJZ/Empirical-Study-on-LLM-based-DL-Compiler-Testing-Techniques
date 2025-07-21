import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(data=[2.0], requires_grad=True)
optimizer = torch.optim.RMSprop([x], lr=0.1, alpha=0.99)
for step in range(10):
    pred = (x ** 2)
    loss = pred.sum()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print('step {}, x = {}, loss = {}'.format(step, x.item(), loss.item()))