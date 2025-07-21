'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones_like\ntorch.ones_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.ones_like(input_data)
print(output_data)