'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
'\nTask 1: Generate input data\n'
input_data = torch.tensor([[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [0, 0, 0, 0]], dtype=torch.bool)
'\nTask 2: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
output = torch.bitwise_xor(input_data, input_data)
print('input_data: ', input_data)
print('output: ', output)