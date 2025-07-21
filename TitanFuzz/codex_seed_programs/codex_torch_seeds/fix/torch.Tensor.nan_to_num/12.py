'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.rand(10, 10)
_input_tensor[(0, 0)] = float('nan')
_input_tensor[(0, 1)] = float('inf')
_input_tensor[(0, 2)] = float('-inf')
_output_tensor = torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)
print(_output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p=2, dim=None, keepdim=False, out=None)\n'
import torch
_input_tensor = torch.rand(10, 10)