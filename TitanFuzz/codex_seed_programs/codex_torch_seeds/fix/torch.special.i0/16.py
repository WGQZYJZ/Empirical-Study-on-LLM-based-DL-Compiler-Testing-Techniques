'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_data = torch.special.i0(input_data)
print('input data:', input_data)
print('output data:', output_data)