'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
data = torch.randn(2, 2)
print(data)
print(torch.tanh(data))