'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
import torch
input = torch.randint(low=0, high=10, size=(5,), dtype=torch.int32)
print('Input: ', input)
result = torch.bitwise_right_shift(input, 2)
print('Result: ', result)
print('Result: ', result)