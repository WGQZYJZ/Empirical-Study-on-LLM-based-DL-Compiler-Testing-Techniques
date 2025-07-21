'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [float('nan'), float('inf'), float('-inf')]])
print('Input:')
print(input_tensor)
print('\nOutput:')
print(torch.Tensor.nan_to_num(input_tensor))