import torch
from torch import nn
from torch.autograd import Variable
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]], requires_grad=True)
Y = torch.tensor([[2.0], [4.0], [6.0], [8.0]], requires_grad=True)
rms = torch.optim.RMSprop([X, Y], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
for i in range(10):
    loss = torch.mean(((X - Y) ** 2))
    loss.backward()
    rms.step()
    rms.zero_grad()