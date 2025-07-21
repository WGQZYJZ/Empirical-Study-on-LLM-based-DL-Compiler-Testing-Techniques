'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.tensor([[True, True, False], [False, False, True]])
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(torch.where(x, y, torch.tensor(0)))