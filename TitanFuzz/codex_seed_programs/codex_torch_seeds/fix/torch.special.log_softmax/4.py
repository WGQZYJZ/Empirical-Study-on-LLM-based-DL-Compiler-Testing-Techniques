'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.log_softmax\ntorch.special.log_softmax(input, dim, *, dtype=None)\n'
import torch
input = torch.randn(1, 5)
print('input:', input)
output = torch.special.log_softmax(input, dim=1)
print('output:', output)