'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros_like\ntorch.zeros_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.arange(1, 11, dtype=torch.float32).reshape(2, 5)
print(input_data)
output_data = torch.zeros_like(input_data)
print(output_data)