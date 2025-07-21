'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.ASGD\ntorch.optim.ASGD(params, lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0)\n'
import torch
import torch.nn as nn
import torch.optim as optim
input_size = 10
output_size = 5
batch_size = 30
hidden_size = 100
x = torch.randn(batch_size, input_size)
y = torch.randn(batch_size, output_size)
model = nn.Linear(input_size, output_size)
optimizer = optim.ASGD(model.parameters(), lr=0.1)
for t in range(500):
    y_pred = model(x)
    loss = torch.nn.functional.mse_loss(y_pred, y)
    print(t, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()