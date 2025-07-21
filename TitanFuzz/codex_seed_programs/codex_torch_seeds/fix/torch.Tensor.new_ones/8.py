'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(3, 4)
output_data = torch.Tensor.new_ones(input_data, size=(3, 4), dtype=torch.double)
print('The input data is: ', input_data)
print('The output data is: ', output_data)