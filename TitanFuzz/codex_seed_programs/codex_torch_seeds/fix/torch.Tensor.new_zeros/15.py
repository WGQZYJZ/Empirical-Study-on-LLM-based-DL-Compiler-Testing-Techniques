'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.new_zeros(input_tensor, (3, 4, 5))
print(output_tensor)