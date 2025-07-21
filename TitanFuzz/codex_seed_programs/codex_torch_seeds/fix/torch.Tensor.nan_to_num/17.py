'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.tensor([[float('nan'), (- 1.0), 0.0, 1.0, float('inf')], [float('nan'), (- 1.0), 0.0, 1.0, float('inf')]])
_output_tensor = torch.Tensor.nan_to_num(_input_tensor)
print('Input Tensor:')
print(_input_tensor)
print('Output Tensor:')
print(_output_tensor)