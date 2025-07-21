"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
data = torch.randn(1, 1, 10, 10)
target = torch.randn(1, 1, 10, 10)
mse_loss = nn.MSELoss()
output = mse_loss(data, target)
print(output)