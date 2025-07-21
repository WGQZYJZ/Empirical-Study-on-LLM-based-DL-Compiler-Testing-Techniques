'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.int8)
print('Input tensor:', input_tensor)
import torch
input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.int8)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.bitwise_left_shift(1)
print('Output tensor:', output_tensor)