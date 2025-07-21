'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
output = torch.concat((a, b), dim=1)
print(output)