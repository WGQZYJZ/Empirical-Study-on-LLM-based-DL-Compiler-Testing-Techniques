'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
x = torch.arange(1, 6, dtype=torch.float)
y = torch.arange(1, 6, dtype=torch.float)
print('x: ', x)
print('y: ', y)
z = torch.Tensor.outer(x, y)
print('z: ', z)