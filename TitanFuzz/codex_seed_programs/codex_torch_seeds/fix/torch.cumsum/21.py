'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = torch.cumsum(input_tensor, dim=0)
print(output_tensor)
output_tensor = torch.cumsum(input_tensor, dim=1)
print(output_tensor)