'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5], dtype=torch.float)
print('x:\n', x)
y = torch.square(x)
print('y:\n', y)