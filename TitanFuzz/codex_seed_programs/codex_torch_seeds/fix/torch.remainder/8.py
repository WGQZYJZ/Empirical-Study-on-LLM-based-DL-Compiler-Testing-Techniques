'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([(- 3.14), (- 2.14), (- 1.14), 0.14, 1.14, 2.14, 3.14])
output_data = torch.remainder(input_data, 2.0)
print('input_data: ', input_data)
print('output_data: ', output_data)