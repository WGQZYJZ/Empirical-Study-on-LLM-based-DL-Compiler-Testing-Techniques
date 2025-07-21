'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(3, 5)
print('input_data:', input_data)
output_data = torch.Tensor.new_ones(input_data, (3, 5))
print('output_data:', output_data)