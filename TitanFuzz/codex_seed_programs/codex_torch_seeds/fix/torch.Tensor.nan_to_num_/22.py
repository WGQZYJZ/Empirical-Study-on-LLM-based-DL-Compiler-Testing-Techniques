'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
import torch
input_tensor = torch.tensor([[float('NaN'), (- float('inf')), float('inf')], [1, 2, 3], [0, 1, 1]])
print('Input Tensor:')
print(input_tensor)
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)
print('Output Tensor:')
print(output_tensor)