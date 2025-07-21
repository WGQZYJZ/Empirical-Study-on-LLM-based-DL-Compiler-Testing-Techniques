'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
print('Task 2: Generate input data')
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor:', input_tensor)
print('Task 3: Call the API torch.Tensor.new_ones')
output_tensor = torch.Tensor.new_ones(input_tensor, [3, 2], dtype=torch.int32)
print('Output tensor:', output_tensor)