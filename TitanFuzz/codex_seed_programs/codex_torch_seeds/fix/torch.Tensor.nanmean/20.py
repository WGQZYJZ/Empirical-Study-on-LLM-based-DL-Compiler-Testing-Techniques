'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmean\ntorch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=0, keepdim=False, dtype=None)
print(output_tensor)