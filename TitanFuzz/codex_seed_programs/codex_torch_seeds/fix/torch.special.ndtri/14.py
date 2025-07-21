'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
input_data = torch.randn(10)
print(input_data)
output = torch.special.ndtri(input_data)
print(output)