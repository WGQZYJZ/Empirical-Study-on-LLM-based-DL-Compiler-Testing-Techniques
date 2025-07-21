'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.div_(input_tensor, 4)
print('Output tensor: ', output_tensor)