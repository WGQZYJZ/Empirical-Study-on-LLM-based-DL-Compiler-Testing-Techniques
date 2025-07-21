'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input Tensor:')
print(input_tensor)
cummin_tensor = torch.Tensor.cummin(input_tensor, dim=1)
print('Cummin Tensor:')
print(cummin_tensor)