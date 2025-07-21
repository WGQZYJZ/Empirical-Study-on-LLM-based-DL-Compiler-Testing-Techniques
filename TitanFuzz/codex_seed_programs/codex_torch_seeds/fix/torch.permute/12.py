'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input = torch.arange(1, 13).view(3, 4)
print('input: ', input)
output = torch.permute(input, (1, 0))
print('output: ', output)