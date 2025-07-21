'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 0, 0], [1, 1, 0]], dtype=torch.bool)
other = torch.tensor([[1, 1, 0], [1, 0, 0]], dtype=torch.bool)
output = torch.bitwise_xor(input, other)
print('input: ', input)
print('other: ', other)
print('output: ', output)