'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
cond = torch.tensor([True, False, False, True], dtype=torch.bool)
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([9, 8, 7, 6])
out = torch.where(cond, x, y)
print(out)