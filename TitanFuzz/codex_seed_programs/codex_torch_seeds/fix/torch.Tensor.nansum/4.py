'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nansum\ntorch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.nansum(input_tensor)
print(output_tensor)