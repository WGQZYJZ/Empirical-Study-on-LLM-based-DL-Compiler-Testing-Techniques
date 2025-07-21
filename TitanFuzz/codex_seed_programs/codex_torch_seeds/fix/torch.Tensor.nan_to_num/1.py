'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.tensor([[float('nan'), float('inf'), float('-inf')], [float('nan'), float('inf'), float('-inf')], [float('nan'), float('inf'), float('-inf')]])
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.Tensor.nan_to_num')
print('torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)')
print('_input_tensor: ', _input_tensor)
_output_tensor = torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)
print('_output_tensor: ', _output_tensor)