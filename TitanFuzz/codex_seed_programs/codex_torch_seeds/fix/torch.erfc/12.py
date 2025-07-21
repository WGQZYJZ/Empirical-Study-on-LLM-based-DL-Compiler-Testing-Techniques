'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfc\ntorch.erfc(input, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
output = torch.erfc(input)
print(output)