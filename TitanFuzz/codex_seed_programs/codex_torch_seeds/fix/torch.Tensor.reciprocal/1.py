'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 2, 3, 4, 5)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.reciprocal()
print('Output tensor:', output_tensor)