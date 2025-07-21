'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, 2)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)