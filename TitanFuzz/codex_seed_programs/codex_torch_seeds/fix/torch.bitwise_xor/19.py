'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
other_data = torch.tensor([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=torch.bool)
output = torch.bitwise_xor(input_data, other_data)
print('input_data: {}'.format(input_data))
print('other_data: {}'.format(other_data))
print('output: {}'.format(output))