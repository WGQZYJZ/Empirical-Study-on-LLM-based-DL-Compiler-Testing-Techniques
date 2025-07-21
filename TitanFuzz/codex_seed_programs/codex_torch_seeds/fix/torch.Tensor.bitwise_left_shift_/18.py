'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.int8)
other = torch.tensor(1, dtype=torch.int8)
output_tensor = input_tensor.bitwise_left_shift_(other)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)