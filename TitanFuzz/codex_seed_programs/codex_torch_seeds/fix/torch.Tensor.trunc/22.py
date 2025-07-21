'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(10)
output_tensor = torch.Tensor.trunc(input_tensor)
print('Input Tensor:', input_tensor)
print('Output Tensor:', output_tensor)