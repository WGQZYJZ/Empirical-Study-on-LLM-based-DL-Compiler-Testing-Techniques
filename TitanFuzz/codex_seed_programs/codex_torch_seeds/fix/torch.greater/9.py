'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
print('PyTorch version: ', torch.__version__)
x = torch.arange(1, 5, dtype=torch.float32)
print('x: ', x)
y = torch.tensor([3.0, 4.0, 4.0, 4.0])
print('y: ', y)
z = torch.greater(x, y)
print('z: ', z)