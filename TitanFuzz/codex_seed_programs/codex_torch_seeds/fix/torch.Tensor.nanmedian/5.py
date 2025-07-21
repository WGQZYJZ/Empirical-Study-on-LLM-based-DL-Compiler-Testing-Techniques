'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
output_tensor = torch.Tensor.nanmedian(input_tensor)
print(output_tensor)