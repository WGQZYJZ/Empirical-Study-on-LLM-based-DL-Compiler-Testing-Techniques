'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SGD\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
y = torch.tensor([[10.0], [20.0]])
linear = nn.Linear(3, 1)
optimizer = optim.SGD([x], lr=0.01)
criterion = nn.MSELoss()
for i in range(10):
    pred = linear(x)
    loss = criterion(pred, y)