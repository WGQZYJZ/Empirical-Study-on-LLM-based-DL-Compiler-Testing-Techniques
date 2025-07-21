'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.new_ones(input_tensor, size=(3, 2))
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)