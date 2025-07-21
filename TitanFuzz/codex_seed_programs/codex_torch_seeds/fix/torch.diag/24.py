'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.arange(9, dtype=torch.float)
print(input_data)
output_data = torch.diag(input_data)
print(output_data)