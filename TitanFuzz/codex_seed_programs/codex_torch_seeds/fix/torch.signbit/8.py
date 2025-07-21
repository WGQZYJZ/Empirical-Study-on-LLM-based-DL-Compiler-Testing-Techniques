'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
print('Input data: ', input_data)
output_data = torch.signbit(input_data)
print('Output data: ', output_data)