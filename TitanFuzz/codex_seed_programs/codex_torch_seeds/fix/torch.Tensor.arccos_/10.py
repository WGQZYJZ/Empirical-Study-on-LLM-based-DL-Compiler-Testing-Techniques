'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos_\ntorch.Tensor.arccos_(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 5)
output_tensor = torch.Tensor.arccos_(input_tensor)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)