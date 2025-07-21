'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.cumprod(_input_tensor, dim=1, dtype=torch.float32)
print('Output tensor: {}'.format(_output_tensor))