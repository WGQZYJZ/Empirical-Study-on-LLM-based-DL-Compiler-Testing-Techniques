'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.randint(0, 10, (2, 3))
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)