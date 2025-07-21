'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
data = torch.tensor([1, 2, 3, 4, 5])
print(data)
print(torch.sigmoid(data))