'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
input = torch.tensor([1, 2, 3])
print(torch.sigmoid(input))