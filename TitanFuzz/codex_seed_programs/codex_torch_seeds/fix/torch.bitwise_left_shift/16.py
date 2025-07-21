'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input_data = torch.randint(low=0, high=10, size=(1, 3, 3, 3), dtype=torch.int32)
print('Input data: ', input_data)
output_data = torch.bitwise_left_shift(input=input_data, other=2)
print('Output data: ', output_data)