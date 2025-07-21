'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igamma\ntorch.igamma(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
other = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
result = torch.igamma(input, other)
print('input: ', input)
print('other: ', other)
print('result: ', result)