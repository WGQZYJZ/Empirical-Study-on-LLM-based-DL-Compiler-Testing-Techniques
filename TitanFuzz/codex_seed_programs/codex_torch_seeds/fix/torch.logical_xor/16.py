'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
x = torch.tensor([False, False, True, True], dtype=torch.bool)
y = torch.tensor([False, True, False, True], dtype=torch.bool)
z = torch.logical_xor(x, y)
print(z)