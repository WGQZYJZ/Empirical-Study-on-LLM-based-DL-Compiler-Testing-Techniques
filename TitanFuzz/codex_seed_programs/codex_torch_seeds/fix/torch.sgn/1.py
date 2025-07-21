'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
sgn_output = torch.sgn(input_data)
print('Input data:', input_data)
print('SGN output:', sgn_output)