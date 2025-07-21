'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.tensor([[1.0, (- 1.0), 2.0], [float('nan'), float('inf'), float('-inf')]])
print(input_tensor)
print(torch.Tensor.nan_to_num_(input_tensor))
print(torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None))
print(torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=1.0, neginf=(- 1.0)))
print(torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=1.0, neginf=1.0))
print(torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=0.0, neginf=0.0))