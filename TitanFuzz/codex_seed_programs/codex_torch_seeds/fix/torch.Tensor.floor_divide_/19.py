'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.arange(1, 5, dtype=torch.float32)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.floor_divide_(2)
print('Output tensor: ', output_tensor)