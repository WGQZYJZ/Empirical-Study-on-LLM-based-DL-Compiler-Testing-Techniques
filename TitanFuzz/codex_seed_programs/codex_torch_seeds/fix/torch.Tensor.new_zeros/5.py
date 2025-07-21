'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
output_data = torch.Tensor.new_zeros(input_data, (2, 3), dtype=None, device=None, requires_grad=False)
print('output_data: ', output_data)