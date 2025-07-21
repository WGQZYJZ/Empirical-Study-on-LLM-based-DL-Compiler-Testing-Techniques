'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.trunc()
print('input_tensor:\n', input_tensor)
print('output_tensor:\n', output_tensor)