'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_tensor = torch.rand(1, 2, 3)
print('Input Tensor:', input_tensor)
output_tensor = torch.log10(input_tensor)
print('Output Tensor:', output_tensor)