'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
print(torch.any((input_data > 0)))
print(torch.any((input_data > 0), dim=0))
print(torch.any((input_data > 0), dim=1))