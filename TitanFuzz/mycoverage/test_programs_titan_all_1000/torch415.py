import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(1.0)
y = torch.tensor(2.0)
w = torch.tensor(1.0, requires_grad=True)
y_hat = (w * x)
y_hat.backward()
x = torch.randn(10, 3)
y = torch.randn(10, 2)
linear = torch.nn.Linear(3, 2)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)
pred = linear(x)
loss = criterion(pred, y)