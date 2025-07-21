'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
input = torch.randn(1, 1, 4, 4)
print('Input: \n', input)
padding = (1, 2, 3, 4)
output = torch.nn.ZeroPad2d(padding)(input)
print('Output: \n', output)