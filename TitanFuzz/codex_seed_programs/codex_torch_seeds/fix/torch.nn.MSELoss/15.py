"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
x = torch.tensor([1.0])
y = torch.tensor([2.0])
loss = torch.nn.MSELoss()
loss = loss(x, y)
print(loss)
print(loss.item())
print(loss.data)
print(loss.data.item())