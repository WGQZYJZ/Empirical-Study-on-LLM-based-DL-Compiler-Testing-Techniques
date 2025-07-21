'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(2, 3)
output_data = torch.Tensor.new_ones(input_data, (2, 3))
print('input_data is: \n', input_data)
print('output_data is: \n', output_data)