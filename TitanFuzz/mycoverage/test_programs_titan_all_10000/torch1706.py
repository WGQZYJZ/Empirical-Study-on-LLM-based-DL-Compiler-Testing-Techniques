import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0, 2.0]])
y = torch.tensor([[2.0]])
linear_regression_model = torch.nn.Linear(2, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(linear_regression_model.parameters(), lr=0.01)
for epoch in range(100):
    y_pred = linear_regression_model(x)
    loss = criterion(y_pred, y)
    print(epoch, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()