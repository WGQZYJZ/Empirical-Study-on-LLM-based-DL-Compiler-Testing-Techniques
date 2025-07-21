'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
x = torch.arange(0, 4)
print('x = ', x)
y = torch.tile(x, (2,))
print('y = ', y)
y = torch.tile(x, (2, 1))
print('y = ', y)
y = torch.tile(x, (2, 2))
print('y = ', y)