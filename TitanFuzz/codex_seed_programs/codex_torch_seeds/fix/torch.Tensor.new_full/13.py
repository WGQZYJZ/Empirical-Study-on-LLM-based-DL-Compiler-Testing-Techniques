'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.new_full(input_tensor, 3, dtype=torch.float32)
print('Output tensor: ', output_tensor)