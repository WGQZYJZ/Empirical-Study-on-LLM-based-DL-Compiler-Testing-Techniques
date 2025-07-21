'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
result = torch.equal(input, other)
print('input:', input)
print('other:', other)
print('result:', result)