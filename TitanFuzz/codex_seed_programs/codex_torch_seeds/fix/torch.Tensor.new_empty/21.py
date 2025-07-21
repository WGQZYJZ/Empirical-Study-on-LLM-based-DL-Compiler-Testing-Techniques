'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
'Task 2: Generate input data'
input_tensor = torch.randn(4, 3)
'Task 3: Call the API torch.Tensor.new_empty'
output_tensor = torch.Tensor.new_empty(input_tensor, (4, 3))
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)