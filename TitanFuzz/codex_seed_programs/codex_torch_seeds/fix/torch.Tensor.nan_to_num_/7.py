'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.Tensor([[1.0, 0.0, 0.0], [0.0, float('nan'), float('inf')], [float('-inf'), float('inf'), float('nan')]])
print('input_tensor: \n', input_tensor)
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)
print('output_tensor: \n', output_tensor)