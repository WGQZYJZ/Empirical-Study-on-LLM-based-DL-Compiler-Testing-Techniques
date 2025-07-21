'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.randn(4, 4)
input_tensor[0][0] = float('nan')
input_tensor[0][1] = float('inf')
input_tensor[0][2] = float('-inf')
input_tensor[1][0] = float('nan')
input_tensor[1][1] = float('inf')
input_tensor[1][2] = float('-inf')
output = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)
print('input_tensor:')
print(input_tensor)
print('output:')
print(output)