'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input = torch.randint(low=0, high=10, size=(4, 4))
other = torch.randint(low=0, high=10, size=(4, 4))
print('Input: ', input)
print('Other: ', other)
print('Result: ', torch.bitwise_left_shift(input, other))