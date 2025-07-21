'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:')
print(input_tensor)
input_tensor[(0, 0)] = float('nan')
input_tensor[(0, 1)] = float('inf')
input_tensor[(0, 2)] = float('-inf')
print('Input Tensor with nan, inf, -inf:')
print(input_tensor)
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)
print('Output Tensor:')
print(output_tensor)