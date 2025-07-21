'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
a = torch.arange(0, 24).view(2, 3, 4)
print('a = ', a)
print('torch.roll(a, 1, 0) = ', torch.roll(a, 1, 0))
print('torch.roll(a, 1, 1) = ', torch.roll(a, 1, 1))
print('torch.roll(a, 1, 2) = ', torch.roll(a, 1, 2))
print('torch.roll(a, -1, 0) = ', torch.roll(a, (- 1), 0))
print('torch.roll(a, -1, 1) = ', torch.roll(a, (- 1), 1))
print('torch.roll(a, -1, 2) = ', torch.roll(a, (- 1), 2))