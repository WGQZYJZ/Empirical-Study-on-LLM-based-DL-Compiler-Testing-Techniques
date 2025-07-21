'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5], dtype=torch.int32)
other = torch.tensor([1, 2, 3, 4, 5], dtype=torch.int32)
output = torch.bitwise_left_shift(input_data, other)
print('Input data: ', input_data)
print('Other: ', other)
print('Output: ', output)