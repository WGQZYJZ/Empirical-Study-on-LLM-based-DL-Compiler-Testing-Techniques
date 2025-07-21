'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(10, 20)
output = torch.std(input_data, dim=1)
print(output)