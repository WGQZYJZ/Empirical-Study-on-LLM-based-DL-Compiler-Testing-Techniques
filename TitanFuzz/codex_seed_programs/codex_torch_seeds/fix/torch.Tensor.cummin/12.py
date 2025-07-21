'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(10, 10)
print('Input Tensor:')
print(input_tensor)
print('\n')
cummin_output_tensor = input_tensor.cummin(dim=1)
print('Output Tensor:')
print(cummin_output_tensor)