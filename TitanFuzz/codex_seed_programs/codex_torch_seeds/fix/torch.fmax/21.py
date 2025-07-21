'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.fmax(input_data, torch.ones(2, 3))
print(output_data)
print(torch.fmax(input_data, torch.ones(2, 3), out=output_data))
print(output_data)