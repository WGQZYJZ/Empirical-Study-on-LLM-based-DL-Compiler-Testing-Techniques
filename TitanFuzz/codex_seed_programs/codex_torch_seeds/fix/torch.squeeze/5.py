'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input_tensor = torch.randn(1, 3, 1, 1)
output_tensor = torch.squeeze(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
print('output_tensor shape:', output_tensor.shape)