'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.le\ntorch.Tensor.le(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = input_tensor.le(0)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)