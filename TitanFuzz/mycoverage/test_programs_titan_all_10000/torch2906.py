import torch
from torch import nn
from torch.autograd import Variable
X = torch.randn(10, 3)
Y = torch.randn(10, 2)
linear = torch.nn.Linear(3, 2)
adamax = torch.optim.Adamax(linear.parameters(), lr=0.01)
criterion = torch.nn.MSELoss()
for epoch in range(100):
    y_pred = linear(X)
    loss = criterion(y_pred, Y)
    print(epoch, loss.item())