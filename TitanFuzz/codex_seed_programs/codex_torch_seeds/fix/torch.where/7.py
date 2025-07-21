'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([6, 7, 8, 9, 10])
condition = (x > 3)
z = torch.where(condition, x, y)
print(z)