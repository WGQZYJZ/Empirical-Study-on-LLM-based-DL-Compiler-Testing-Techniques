'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('\tPyTorch version:', torch.__version__)
print('\nTask 2: Generate input data')
input = torch.randn(4, 4)
print('\tInput:', input)
print('\nTask 3: Call the API torch.le')
output = torch.le(input, 0)
print('\tOutput:', output)
print('\nTask 4: Call the API torch.le with out')
output_with_out = torch.empty(4, 4)
torch.le(input, 0, out=output_with_out)
print('\tOutput with out:', output_with_out)