'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nextafter\ntorch.Tensor.nextafter(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
output_tensor = input_tensor.nextafter(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)