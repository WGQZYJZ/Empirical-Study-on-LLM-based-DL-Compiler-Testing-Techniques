'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.abs_\ntorch.Tensor.abs_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.abs_(input_tensor)
print('Input Tensor:')
print(input_tensor)
print('Output Tensor:')
print(output_tensor)