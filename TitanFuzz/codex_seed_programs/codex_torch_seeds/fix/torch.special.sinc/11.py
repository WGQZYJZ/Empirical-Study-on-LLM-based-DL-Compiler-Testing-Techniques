'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.sinc\ntorch.special.sinc(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
sinc_output = torch.special.sinc(input)
print('Input: \n', input)
print('Output: \n', sinc_output)