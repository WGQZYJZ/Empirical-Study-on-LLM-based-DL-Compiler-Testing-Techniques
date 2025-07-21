'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = input_tensor.cumprod(dim=1)
print(output_tensor)