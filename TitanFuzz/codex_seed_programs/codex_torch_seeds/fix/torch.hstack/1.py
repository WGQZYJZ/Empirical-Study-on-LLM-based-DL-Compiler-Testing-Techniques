'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
print(torch.hstack([x, y]))