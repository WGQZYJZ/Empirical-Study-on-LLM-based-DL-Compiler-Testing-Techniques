'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input = torch.rand(4, 3)
vec = torch.rand(3)
output = torch.mv(input, vec)
print('\ninput:')
print(input)
print('\nvec:')
print(vec)
print('\noutput:')
print(output)