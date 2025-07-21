'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1.0), 0.0, 1.0])
output = torch.sgn(input_data)
print('The output tensor: ', output)