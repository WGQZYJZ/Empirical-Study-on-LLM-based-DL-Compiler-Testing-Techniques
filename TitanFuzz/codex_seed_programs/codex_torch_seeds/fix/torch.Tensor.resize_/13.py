'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(5, 6)
print('input_tensor:', input_tensor)
print('input_tensor.size():', input_tensor.size())
print('\nTask 3: Call the API torch.Tensor.resize_')
print('torch.Tensor.resize_(input_tensor, *sizes, memory_format=torch.contiguous_format)')
print('input_tensor.resize_(3, 2):', input_tensor.resize_(3, 2))
print('input_tensor:', input_tensor)
print('input_tensor.size():', input_tensor.size())
print('\nTask 4: Call the API torch.Tensor.resize_as_')
print('torch.Tensor.resize_as_(input, tensor)')
input_tensor2 = torch.randn(4, 3)
print('input_tensor2:', input_tensor2)