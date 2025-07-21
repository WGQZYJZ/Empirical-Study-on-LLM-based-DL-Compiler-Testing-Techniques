'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(input_tensor)
cummin_tensor = input_tensor.cummin(dim=0)
print('Cummin tensor:')
print(cummin_tensor)