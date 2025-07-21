'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
output = torch.equal(x, y)
print('x:', x)
print('y:', y)
print('output:', output)