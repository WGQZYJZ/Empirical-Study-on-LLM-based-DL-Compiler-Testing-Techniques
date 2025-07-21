'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.triu(input_data, diagonal=0)
torch.tril(input_data, diagonal=0)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.tril(input_data, diagonal=0)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)