'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
output = torch.Tensor.is_conj(input_tensor)
print('input_tensor:', input_tensor)
print('output:', output)