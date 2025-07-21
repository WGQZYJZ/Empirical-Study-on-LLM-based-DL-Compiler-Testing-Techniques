'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.msort\ntorch.msort(input, *, out=None)\n'
import torch
input_data = torch.randn(10, 3)
print(input_data)
output = torch.msort(input_data)
print(output)