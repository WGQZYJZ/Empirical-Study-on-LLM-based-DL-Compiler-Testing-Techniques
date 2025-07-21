'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot_\ntorch.Tensor.hypot_(_input_tensor, other)\n'
import torch
input_data = torch.tensor([[3, 4], [5, 6]])
other_data = torch.tensor([[4, 3], [6, 5]])
print('input_data: ', input_data)
print('other_data: ', other_data)
output_data = torch.Tensor.hypot_(input_data, other_data)
print('output_data: ', output_data)