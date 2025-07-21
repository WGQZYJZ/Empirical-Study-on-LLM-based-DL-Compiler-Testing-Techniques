'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
input = torch.randint(low=0, high=10, size=(3, 5), dtype=torch.int32)
print('input =\n', input)
output = torch.cummax(input, dim=1)
print('output =\n', output)