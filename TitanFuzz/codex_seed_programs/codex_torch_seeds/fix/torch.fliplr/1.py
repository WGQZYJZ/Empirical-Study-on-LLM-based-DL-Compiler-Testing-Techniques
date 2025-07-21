'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input = torch.rand(4, 4)
print('Input: \n', input)
output = torch.fliplr(input)
print('Output: \n', output)