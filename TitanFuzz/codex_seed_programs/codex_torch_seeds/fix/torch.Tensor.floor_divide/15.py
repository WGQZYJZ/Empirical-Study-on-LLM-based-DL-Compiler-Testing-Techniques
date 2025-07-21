'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[2, 4, 6], [8, 10, 12]])
output_tensor = torch.Tensor.floor_divide(input_tensor, 2)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)