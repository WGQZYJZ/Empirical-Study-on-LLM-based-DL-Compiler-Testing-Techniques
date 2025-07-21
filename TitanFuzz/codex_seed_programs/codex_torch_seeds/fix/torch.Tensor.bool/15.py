'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.bool()
print('Output tensor: ', output_tensor)