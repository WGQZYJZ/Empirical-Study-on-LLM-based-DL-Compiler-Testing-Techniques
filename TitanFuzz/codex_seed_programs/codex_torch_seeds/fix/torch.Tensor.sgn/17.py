'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn\ntorch.Tensor.sgn(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 1)
output_tensor = input_tensor.sgn()
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)