'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.ones(5, 3)
print('Input data:', input_data)
output_data = torch.Tensor.new_empty(input_data, (5, 3), dtype=torch.int32)
print('Output data:', output_data)