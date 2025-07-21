'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erf\ntorch.erf(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1.0), 0.0, 1.0])
output = torch.erf(input_data)
print('Input: ', input_data)
print('Output: ', output)