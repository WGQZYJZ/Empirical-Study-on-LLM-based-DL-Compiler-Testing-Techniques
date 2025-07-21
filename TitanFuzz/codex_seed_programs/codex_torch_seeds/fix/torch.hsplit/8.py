'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
x = torch.arange(16, dtype=torch.float32).reshape(4, 4)
print('Input data: ', x)
y = torch.hsplit(x, 2)
print('Result: ', y)