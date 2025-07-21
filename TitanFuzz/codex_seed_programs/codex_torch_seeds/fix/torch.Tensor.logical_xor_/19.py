'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([True, False, True, False])
other = torch.tensor([True, True, False, False])
output_tensor = input_tensor.logical_xor_(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)