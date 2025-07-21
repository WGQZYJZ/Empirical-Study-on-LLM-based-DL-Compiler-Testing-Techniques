'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0])
y = torch.square(x)
print('x = ', x)
print('y = ', y)