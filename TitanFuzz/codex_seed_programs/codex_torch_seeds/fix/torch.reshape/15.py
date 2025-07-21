'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
x = torch.randn(4, 4)
print(x)
y = torch.reshape(x, (8, 2))
print(y)