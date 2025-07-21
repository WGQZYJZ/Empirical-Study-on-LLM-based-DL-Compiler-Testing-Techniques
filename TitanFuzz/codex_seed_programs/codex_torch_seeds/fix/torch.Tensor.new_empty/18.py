'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
output_data = torch.Tensor.new_empty(input_data, size=(3, 4), dtype=torch.int64, device=None, requires_grad=False)
print(output_data)