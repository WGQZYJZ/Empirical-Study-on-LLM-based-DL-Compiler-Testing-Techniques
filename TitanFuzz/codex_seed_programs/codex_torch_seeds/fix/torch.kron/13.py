'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.kron(input, other)
print('Input: \n', input)
print('Other: \n', other)
print('Output: \n', output)