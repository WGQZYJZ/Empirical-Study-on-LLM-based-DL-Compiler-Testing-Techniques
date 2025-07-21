'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 2)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.reciprocal()
print('Output tensor:', output_tensor)