'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.cumprod(input_tensor, dim=1)
print(output_tensor)