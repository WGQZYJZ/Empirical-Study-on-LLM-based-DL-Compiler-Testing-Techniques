'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 5)
other_tensor = torch.randn(3, 5)
output_tensor = input_tensor.subtract(other_tensor)
print('input_tensor:', input_tensor)
print('other_tensor:', other_tensor)
print('output_tensor:', output_tensor)
'\nTask 4: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
output_tensor = input_tensor.subtract(other_tensor, alpha=2)
print('input_tensor:', input_tensor)
print('other_tensor:', other_tensor)
print('output_tensor:', output_tensor)