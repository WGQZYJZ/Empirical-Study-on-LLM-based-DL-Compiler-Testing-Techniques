'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
print('The input data is:', input_data)
output = torch.arctanh(input_data)
print('The output is:', output)