'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(4, 4)
input_tensor[(1, 1)] = float('nan')
input_tensor[(2, 2)] = float('nan')
print(input_tensor)
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)
print(output_tensor)