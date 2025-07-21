'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)