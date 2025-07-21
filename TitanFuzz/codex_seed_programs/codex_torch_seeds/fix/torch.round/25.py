'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input = torch.tensor([(- 1.9), (- 1.5), (- 1.2), (- 0.8), (- 0.4), 0.0, 0.4, 0.8, 1.2, 1.5, 1.9])
output = torch.round(input)
print('input: {}'.format(input))
print('output: {}'.format(output))