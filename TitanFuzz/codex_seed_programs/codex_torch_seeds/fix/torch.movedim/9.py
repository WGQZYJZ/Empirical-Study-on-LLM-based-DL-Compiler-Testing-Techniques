'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input = torch.randn(2, 3, 4)
print('input size:', input.size())
output = torch.movedim(input, 0, 1)
print('output size:', output.size())