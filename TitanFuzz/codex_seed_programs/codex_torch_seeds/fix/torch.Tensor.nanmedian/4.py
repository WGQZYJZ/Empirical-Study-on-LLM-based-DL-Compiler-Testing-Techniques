'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 4)
input_tensor[(2, 2)] = float('nan')
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=True)
print(output_tensor)