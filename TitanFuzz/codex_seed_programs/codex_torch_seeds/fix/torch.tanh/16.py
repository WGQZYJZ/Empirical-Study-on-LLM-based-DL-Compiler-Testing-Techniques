'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
output = torch.tanh(input)
print(output)