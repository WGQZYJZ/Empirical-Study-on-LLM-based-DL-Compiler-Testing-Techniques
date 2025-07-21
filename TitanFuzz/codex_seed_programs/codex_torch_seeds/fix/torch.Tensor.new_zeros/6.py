'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_tensor = torch.Tensor(input_data)
output_tensor = torch.Tensor.new_zeros(input_tensor, (1, 3))
print('The input tensor is: ', input_tensor)
print('The output tensor is: ', output_tensor)