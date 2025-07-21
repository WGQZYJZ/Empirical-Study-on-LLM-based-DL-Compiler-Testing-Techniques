'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
input_tensor = torch.randn(4, 3, 2)
print('Input Tensor:', input_tensor)
input_tensor = torch.randn(4, 3, 2)
print('Input Tensor:', input_tensor)
output_tensor = input_tensor.permute(2, 0, 1)
print('Output Tensor:', output_tensor)