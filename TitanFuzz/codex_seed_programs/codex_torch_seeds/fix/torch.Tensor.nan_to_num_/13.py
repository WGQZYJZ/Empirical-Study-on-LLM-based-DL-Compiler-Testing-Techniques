'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.tensor([[float('nan'), float('-inf'), float('inf')], [1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print('input_tensor: ', input_tensor)
nan_to_num_input = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)
print('nan_to_num_input: ', nan_to_num_input)