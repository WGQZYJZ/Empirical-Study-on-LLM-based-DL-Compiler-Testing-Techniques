'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
input = torch.randn(2, 3)
print('Input: ', input)
output = torch.nn.Softmin(dim=1)(input)
print('Output: ', output)