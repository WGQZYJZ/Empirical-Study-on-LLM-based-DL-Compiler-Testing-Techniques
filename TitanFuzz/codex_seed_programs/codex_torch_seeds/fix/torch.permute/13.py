'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input = torch.arange(0, 12).view(3, 4)
print('Input: ', input)
output = torch.permute(input, (1, 0))
print('Output: ', output)
output = torch.t(input)
print('Output: ', output)