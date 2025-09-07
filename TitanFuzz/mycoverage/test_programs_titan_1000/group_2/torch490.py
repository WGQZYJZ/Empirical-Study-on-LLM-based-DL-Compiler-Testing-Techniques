import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0)
optimizer = torch.optim.NAdam([x], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
for i in range(10):
    y_hat = (x * x)
    loss = ((y_hat - y) ** 2)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print('step {}: x = {}, x-squared = {}'.format(i, x.item(), y_hat.item()))