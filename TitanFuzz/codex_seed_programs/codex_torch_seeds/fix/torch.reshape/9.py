'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
x = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
y = torch.reshape(x, (2, 6))
print('x = \n', x)
print('y = \n', y)