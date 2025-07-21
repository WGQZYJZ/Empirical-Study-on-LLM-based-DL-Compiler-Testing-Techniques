'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(4, 3)
print(input)
output = torch.tril(input)
print(output)