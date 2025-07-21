'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.new_full(input_tensor, 4, 10, dtype=torch.int32)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)