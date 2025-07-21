'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.new_zeros(input_tensor, size=(2, 3), dtype=None, device=None, requires_grad=False)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)