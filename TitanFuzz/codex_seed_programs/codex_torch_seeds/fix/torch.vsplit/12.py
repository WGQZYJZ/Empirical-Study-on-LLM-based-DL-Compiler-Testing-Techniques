'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
input = torch.arange(start=0, end=18, step=1).view(3, 2, 3)
print('input: \n', input)
indices_or_sections = [2, 2]
output = torch.vsplit(input, indices_or_sections)
print('output: \n', output)