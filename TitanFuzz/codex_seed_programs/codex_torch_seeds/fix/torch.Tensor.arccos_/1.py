'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos_\ntorch.Tensor.arccos_(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.arccos_(input_tensor)
print('Output tensor: ', output_tensor)