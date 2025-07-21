'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.int32)
print('Input data: {}'.format(input_data))
output_data = torch.bitwise_xor(input_data, input_data)
print('Output data: {}'.format(output_data))