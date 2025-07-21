'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
condition = torch.tensor([[True, False], [True, False]], dtype=torch.bool)
print('x:', x)
print('y:', y)
print('condition:', condition)
print('torch.where(condition, x, y):', torch.where(condition, x, y))