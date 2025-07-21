'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift_\ntorch.Tensor.bitwise_right_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, 2)
print('output_tensor: ', output_tensor)