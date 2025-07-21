'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_tensor = torch.Tensor(input_data)
output_tensor = torch.Tensor.new_tensor(input_tensor, input_data)
print('Input data: ', input_data)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)