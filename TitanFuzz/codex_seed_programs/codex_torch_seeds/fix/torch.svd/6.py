'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
input_data = torch.randn(10, 5)
print(input_data)
output_data = torch.svd(input_data)
print(output_data)