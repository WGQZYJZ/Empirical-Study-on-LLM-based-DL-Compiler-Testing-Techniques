'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_like\ntorch.empty_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.rand(3, 3)
print(input_data)
output_data = torch.empty_like(input_data)
print(output_data)
output_data = torch.zeros_like(input_data)
print(output_data)
output_data = torch.ones_like(input_data)
print(output_data)