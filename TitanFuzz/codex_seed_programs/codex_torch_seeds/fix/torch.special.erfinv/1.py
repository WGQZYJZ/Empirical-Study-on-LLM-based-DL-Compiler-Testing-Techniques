'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(input_data)
output = torch.special.erfinv(input_data)
print(output)