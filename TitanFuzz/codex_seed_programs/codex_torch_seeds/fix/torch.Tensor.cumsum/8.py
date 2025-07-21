'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(4, 3)
print(input_tensor)
output_tensor = input_tensor.cumsum(dim=1)
print(output_tensor)