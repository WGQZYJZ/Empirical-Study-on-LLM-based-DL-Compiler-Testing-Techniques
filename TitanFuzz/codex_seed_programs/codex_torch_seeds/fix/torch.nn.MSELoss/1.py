"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = torch.tensor([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
mse_loss = nn.MSELoss()
loss = mse_loss(x, y)
print(loss)