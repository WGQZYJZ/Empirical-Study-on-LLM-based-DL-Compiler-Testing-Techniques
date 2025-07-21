'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('x = ', x)
x_narrow = torch.narrow(x, 1, 0, 2)
print('x_narrow = ', x_narrow)