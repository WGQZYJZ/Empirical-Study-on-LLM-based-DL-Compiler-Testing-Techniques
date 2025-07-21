'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RMSprop\ntorch.optim.RMSprop(params, lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
x = torch.randn(10, 5)
y = torch.randn(10, 5)
linear = nn.Linear(5, 5)
print('w: ', linear.weight)
print('b: ', linear.bias)
criterion = nn.MSELoss()
optimizer = optim.RMSprop(linear.parameters(), lr=0.01)
optimizer_momentum = optim.RMSprop(linear.parameters(), lr=0.01, momentum=0.9)