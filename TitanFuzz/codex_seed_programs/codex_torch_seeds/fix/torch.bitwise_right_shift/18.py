'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(low=0, high=10, size=(3, 3))
print('input: ', input)
other = torch.randint(low=0, high=10, size=(3, 3))
print('other: ', other)
output = torch.bitwise_right_shift(input, other)
print('output: ', output)