'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(3, 3)
print(input_data)
output_data = torch.Tensor.new_full(input_data, 3, fill_value=1, dtype=None, device=None, requires_grad=False)
print(output_data)