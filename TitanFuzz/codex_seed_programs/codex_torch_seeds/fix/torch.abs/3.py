'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 2), 3, 4, (- 5), (- 6), 7, 8], dtype=torch.float32)
print('Input data: ', input_data)
abs_data = torch.abs(input_data)
print('Absolute data: ', abs_data)