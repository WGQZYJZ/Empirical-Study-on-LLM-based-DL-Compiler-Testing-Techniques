'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
x = torch.tensor([1, 0, 1, 0], dtype=torch.bool)
print('Input data:', x)
out = torch.bitwise_not(x)
print('Output data:', out)