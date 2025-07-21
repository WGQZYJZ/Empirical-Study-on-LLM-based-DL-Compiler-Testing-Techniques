'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_data = torch.tensor([0, 1, 1, 0], dtype=torch.bool)
print('Input data: ', input_data)
output_data = torch.bitwise_not(input_data)
print('Output data: ', output_data)