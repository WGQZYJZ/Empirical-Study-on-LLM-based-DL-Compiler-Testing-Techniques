'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.ASGD\ntorch.optim.ASGD(params, lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
data = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1.0]], requires_grad=True)
target = torch.tensor([[0], [0], [1], [1.0]], requires_grad=True)
model = nn.Linear(2, 1)
optimizer = optim.ASGD(model.parameters(), lr=0.1)
for iter in range(20):
    optimizer.zero_grad()
    pred = model(data)
    loss = ((pred - target) ** 2).sum()
    loss.backward()