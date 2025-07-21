"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch
input = torch.randn(1, 3, 10, 10)
target = torch.randn(1, 3, 10, 10)
loss = torch.nn.MSELoss()
loss_value = loss(input, target)
print(loss_value)