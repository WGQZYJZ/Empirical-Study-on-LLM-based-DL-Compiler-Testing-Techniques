'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input = torch.randn(3, 5)
print('Input data: ', input)
result = torch.narrow(input, 1, 2, 3)
print('Result: ', result)