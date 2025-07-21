'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
input_data = torch.randint(low=0, high=100, size=(1,), dtype=torch.int8)
print('Input data: ', input_data)
output_data = torch.bitwise_right_shift(input_data, 2, out=None)
print('Output data: ', output_data)