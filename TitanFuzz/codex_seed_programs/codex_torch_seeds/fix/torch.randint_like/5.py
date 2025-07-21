'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint_like\ntorch.randint_like(input, low=0, high, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(10, 10)
output_data = torch.randint_like(input_data, low=0, high=10, dtype=torch.int32)
print(input_data)
print(output_data)