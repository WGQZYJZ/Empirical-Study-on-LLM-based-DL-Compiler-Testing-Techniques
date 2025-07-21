'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.ASGD\ntorch.optim.ASGD(params, lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
data = torch.randn(1, 1)
target = torch.Tensor([[0]])
model = nn.Linear(1, 1)
optimizer = optim.ASGD(model.parameters(), lr=0.01)
for i in range(100):
    optimizer.zero_grad()
    output = model(data)
    loss = F.mse_loss(output, target)
    loss.backward()
    optimizer.step()
    print(loss.item())