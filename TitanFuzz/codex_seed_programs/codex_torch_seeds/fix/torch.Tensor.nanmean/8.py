'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmean\ntorch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=torch.float32)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.nanmean(input_tensor)
print('output_tensor: ', output_tensor)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=0)
print('output_tensor: ', output_tensor)
output_tensor = torch.Tensor.nanmean(input_tensor, dim=1)
print('output_tensor: ', output_tensor)