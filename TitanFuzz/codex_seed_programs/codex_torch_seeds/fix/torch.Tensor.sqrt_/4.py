'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt_\ntorch.Tensor.sqrt_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
print('Input: \n', input_tensor)
output_tensor = torch.Tensor.sqrt_(input_tensor)
print('Output: \n', output_tensor)