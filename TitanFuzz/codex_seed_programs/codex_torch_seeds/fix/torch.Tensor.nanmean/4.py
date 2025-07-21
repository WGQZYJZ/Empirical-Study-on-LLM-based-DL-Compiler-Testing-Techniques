'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmean\ntorch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
input_tensor[(1, 1)] = torch.nan
print('input_tensor:\n', input_tensor)
mean_value = torch.Tensor.nanmean(input_tensor)
print('mean_value:\n', mean_value)
mean_value = torch.Tensor.nanmean(input_tensor, dim=0)
print('mean_value:\n', mean_value)
mean_value = torch.Tensor.nanmean(input_tensor, dim=1)
print('mean_value:\n', mean_value)