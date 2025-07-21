'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat\ntorch.Tensor.repeat(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = input_tensor.repeat(2, 3)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)