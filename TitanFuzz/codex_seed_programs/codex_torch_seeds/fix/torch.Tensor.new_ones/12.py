'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.rand(5, 3)
output_tensor = torch.Tensor.new_ones(input_tensor, (5, 3))
print('The result of torch.Tensor.new_ones is: ', output_tensor)