'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(10, 10)
print(input_data)
output = torch.diag(input_data)
print(output)
output = torch.diag_embed(input_data)
print(output)
output = torch.diagflat(input_data)
print(output)