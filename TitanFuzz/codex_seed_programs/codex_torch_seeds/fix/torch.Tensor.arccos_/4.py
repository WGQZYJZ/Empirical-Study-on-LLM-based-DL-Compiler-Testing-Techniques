'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos_\ntorch.Tensor.arccos_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.arccos_(input_tensor)
print('Output Tensor: ', output_tensor)