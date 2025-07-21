'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj\ntorch.Tensor.conj(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.conj(input_tensor)
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)