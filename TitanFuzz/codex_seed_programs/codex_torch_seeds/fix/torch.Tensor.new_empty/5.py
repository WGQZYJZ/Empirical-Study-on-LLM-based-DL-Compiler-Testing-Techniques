'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
output_tensor = torch.Tensor.new_empty(input_tensor, (2, 2, 2))
print(output_tensor)