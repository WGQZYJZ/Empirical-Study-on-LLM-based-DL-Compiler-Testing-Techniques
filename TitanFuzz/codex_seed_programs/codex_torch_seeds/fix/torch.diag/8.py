'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.arange(1, 7).reshape(2, 3)
print(input)
diag = torch.diag(input)
print(diag)