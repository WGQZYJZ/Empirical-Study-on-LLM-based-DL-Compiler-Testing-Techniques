'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
input = torch.tensor([[1, 1, 1], [0, 0, 0]], dtype=torch.bool)
output = torch.logical_not(input)
print(output)