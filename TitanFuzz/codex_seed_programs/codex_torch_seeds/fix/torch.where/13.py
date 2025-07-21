'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
cond = torch.tensor([True, False])
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
print(torch.where(cond, x, y))
cond = torch.tensor([[True, False], [True, False]])
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
print(torch.where(cond, x, y))
cond = torch.tensor([[[True, False], [True, False]], [[True, False], [True, False]]])
x = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
y = torch.tensor([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])