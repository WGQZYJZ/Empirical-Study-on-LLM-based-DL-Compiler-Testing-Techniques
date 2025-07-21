'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.int32)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, 2)
print('Output tensor: ', output_tensor)