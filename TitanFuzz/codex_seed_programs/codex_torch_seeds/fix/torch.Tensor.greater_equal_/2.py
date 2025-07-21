'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater_equal_\ntorch.Tensor.greater_equal_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.greater_equal_(input_tensor, 0)
print('Output tensor: ', output_tensor)