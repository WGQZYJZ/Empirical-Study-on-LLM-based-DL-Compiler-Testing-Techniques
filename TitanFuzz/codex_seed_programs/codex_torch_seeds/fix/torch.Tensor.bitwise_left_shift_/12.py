'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(2, 2), dtype=torch.int8)
other = torch.randint(low=0, high=2, size=(2, 2), dtype=torch.int8)
print('Input tensor:', input_tensor)
print('Other tensor:', other)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, other)
print('Output tensor:', output_tensor)