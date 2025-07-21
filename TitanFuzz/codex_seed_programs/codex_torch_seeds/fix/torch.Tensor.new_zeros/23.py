'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.new_zeros(input_tensor, (3, 3))
print('The input tensor is: {}'.format(input_tensor))
print('The output tensor is: {}'.format(output_tensor))