'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asin\ntorch.Tensor.asin(_input_tensor)\n'
import torch
input_tensor = torch.rand(10)
output_tensor = input_tensor.asin()
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)