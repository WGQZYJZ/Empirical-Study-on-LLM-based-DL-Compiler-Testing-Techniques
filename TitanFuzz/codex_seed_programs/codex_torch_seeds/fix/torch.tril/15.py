'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print(input_data)
print(torch.tril(input_data))