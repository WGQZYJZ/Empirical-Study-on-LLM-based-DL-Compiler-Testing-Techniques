'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print('Input: ', input)
print('Output: ', torch.lgamma(input))
'\nOutput: \nInput:  tensor([1., 2., 3., 4., 5.])\nOutput:  tensor([ 0.0000,  0.9189,  1.7918,  3.1781,  4.5722])\n'