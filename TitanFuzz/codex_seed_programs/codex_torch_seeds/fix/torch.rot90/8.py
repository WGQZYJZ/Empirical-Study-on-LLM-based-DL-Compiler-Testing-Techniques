'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
x = torch.randint(0, 10, (4, 5))
print('x =', x)
y = torch.rot90(x, 3, dims=(0, 1))
print('y =', y)