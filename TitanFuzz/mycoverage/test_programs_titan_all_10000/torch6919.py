import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10, requires_grad=True)
optimizer = torch.optim.Rprop(params=[data], lr=0.01, etas=(0.5, 1.2), step_sizes=(1e-06, 50))
for i in range(10):
    optimizer.zero_grad()
    output = data.sigmoid()
    loss = output.sum()
    loss.backward()
    optimizer.step()
    print(loss)
    print(data)
    print(data.grad)