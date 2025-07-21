import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0], [2.0], [3.0]], requires_grad=True)
y = torch.tensor([[2.0], [4.0], [6.0]])
rmsprop = torch.optim.RMSprop([x], lr=0.01, alpha=0.99)
for i in range(100):
    y_pred = (x * 2)
    loss = torch.mean(((y_pred - y) ** 2))
    print(i, loss.data.item())
    rmsprop.zero_grad()
    loss.backward()
    rmsprop.step()