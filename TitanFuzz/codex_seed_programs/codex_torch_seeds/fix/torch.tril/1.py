'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
print(torch.__version__)
input = torch.randn(3, 3)
print(input)
print(torch.tril(input))