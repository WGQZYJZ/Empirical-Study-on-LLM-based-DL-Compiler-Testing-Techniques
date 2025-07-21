'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input = torch.tensor([0, 2, 4, 6, 8])
other = torch.tensor([1, 2, 3, 4, 5])
output = torch.bitwise_left_shift(input, other)
print('Input: ', input)
print('Other: ', other)
print('Output: ', output)