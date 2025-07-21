'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full_like\ntorch.full_like(input, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
import torch
input = torch.randint(10, (2, 3), dtype=torch.int32)
print('Input data: ', input)
output = torch.full_like(input, fill_value=0, dtype=torch.float32)
print('Output data: ', output)