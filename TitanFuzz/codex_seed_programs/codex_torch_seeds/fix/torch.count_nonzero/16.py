'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input = torch.randn(4, 4)
input[(0, 0)] = 0
input[(1, 1)] = 0
input[(2, 2)] = 0
input[(3, 3)] = 0
print(input)
print(torch.count_nonzero(input))
print(torch.count_nonzero(input, dim=0))
print(torch.count_nonzero(input, dim=1))
print(input.nonzero())
print(input.nonzero().size())