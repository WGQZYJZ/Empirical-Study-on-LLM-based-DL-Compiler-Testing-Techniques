'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input = torch.randn(2, 3)
print('input =', input)
output = torch.reshape(input, (6, 1))
print('output =', output)
output = torch.reshape(input, (3, 2))
print('output =', output)
output = torch.reshape(input, (1, 6))
print('output =', output)