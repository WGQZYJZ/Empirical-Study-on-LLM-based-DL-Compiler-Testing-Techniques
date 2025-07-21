'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
condition = torch.tensor([True, False])
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
out = torch.where(condition, x, y)
print(out)