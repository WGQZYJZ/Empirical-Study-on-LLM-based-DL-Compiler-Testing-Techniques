'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
x = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]])
y = torch.tensor([[4, 3, 2], [2, 3, 4]])
z = torch.div(x, y)
print('x =', x)
print('y =', y)
print('z =', z)