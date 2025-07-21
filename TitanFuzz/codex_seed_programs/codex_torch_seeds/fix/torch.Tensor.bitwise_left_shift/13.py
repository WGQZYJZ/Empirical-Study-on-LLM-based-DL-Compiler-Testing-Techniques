'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
other = torch.tensor(2, dtype=torch.uint8)
output_tensor = input_tensor.bitwise_left_shift(other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('output_tensor: ', output_tensor)