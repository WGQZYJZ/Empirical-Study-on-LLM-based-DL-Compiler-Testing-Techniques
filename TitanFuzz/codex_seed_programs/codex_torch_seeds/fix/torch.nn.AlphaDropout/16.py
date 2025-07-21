'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
input = torch.randn(10, 10)
alphaDropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = alphaDropout(input)
print('Input: ', input)
print('Output: ', output)