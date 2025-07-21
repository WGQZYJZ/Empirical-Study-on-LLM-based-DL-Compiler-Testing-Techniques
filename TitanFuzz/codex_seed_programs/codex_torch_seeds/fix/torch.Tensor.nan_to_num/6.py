'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.rand(4, 4)
input_tensor[(1, 1)] = float('nan')
input_tensor[(2, 2)] = float('inf')
input_tensor[(3, 3)] = float('-inf')
output_tensor = torch.Tensor.nan_to_num(input_tensor, nan=0.0, posinf=None, neginf=None)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)