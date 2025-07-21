'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinc\ntorch.Tensor.sinc(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 3)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.sinc(input_tensor)
print('output_tensor:', output_tensor)