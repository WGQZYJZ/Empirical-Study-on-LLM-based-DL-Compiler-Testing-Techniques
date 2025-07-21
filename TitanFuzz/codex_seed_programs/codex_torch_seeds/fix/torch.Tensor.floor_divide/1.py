'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.floor_divide(input_tensor, 2)
print('Output tensor: ', output_tensor)