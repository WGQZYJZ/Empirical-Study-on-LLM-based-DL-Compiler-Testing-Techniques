'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
input = torch.randn(3, 3)
A = torch.randn(3, 3)
output = torch.lstsq(input, A)
print(output)