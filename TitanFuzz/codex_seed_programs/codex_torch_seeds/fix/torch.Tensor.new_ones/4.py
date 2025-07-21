'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.new_ones(input_tensor, (1, 3), dtype=torch.float32, device=None, requires_grad=False)
print(output_tensor)