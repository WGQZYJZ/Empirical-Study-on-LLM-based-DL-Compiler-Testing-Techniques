'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.tensor([[float('nan'), float('inf'), float('-inf')], [1, 2, 3], [float('nan'), float('inf'), float('-inf')]])
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)
print('Output tensor:')
print(output_tensor)