'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
x = torch.tensor([[[1], [2], [3]], [[4], [5], [6]]])
y = torch.squeeze(x)
print(y)