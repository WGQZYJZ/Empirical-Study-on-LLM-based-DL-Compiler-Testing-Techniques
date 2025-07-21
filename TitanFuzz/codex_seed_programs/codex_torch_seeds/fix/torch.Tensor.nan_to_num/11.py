'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
_input_tensor[(_input_tensor == 5)] = float('nan')
_input_tensor[(_input_tensor == 6)] = float('inf')
_input_tensor[(_input_tensor == 7)] = float('-inf')
print(_input_tensor)
print(torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None))
print(torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=0.0, neginf=None))
print(torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=0.0))