'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.random_\ntorch.Tensor.random_(_input_tensor, from=0, to=None, *, generator=None)\n'
import torch
input_tensor = torch.arange(0, 12, dtype=torch.float32)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.random_(input_tensor)
print('Output tensor: ', output_tensor)