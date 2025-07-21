'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [float('nan'), float('nan'), float('nan')]], dtype=torch.float)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.nan_to_num(input_tensor, nan=0.0, posinf=None, neginf=None)
print('Output tensor: \n', output_tensor)