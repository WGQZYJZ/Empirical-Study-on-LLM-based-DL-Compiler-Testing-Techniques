'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.arange(1, 11, dtype=torch.float)
print('input_tensor: ', input_tensor)
torch.Tensor.divide_(input_tensor, 2)
print('output_tensor: ', input_tensor)
torch.Tensor.divide_(input_tensor, 2, rounding_mode='floor')
print('output_tensor: ', input_tensor)
torch.Tensor.divide_(input_tensor, 2, rounding_mode='ceil')
print('output_tensor: ', input_tensor)
torch.Tensor.divide_(input_tensor, 2, rounding_mode='trunc')