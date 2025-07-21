'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input = torch.tensor([0.2, 0.4, 0.6, 0.8, 1.0])
boundaries = torch.tensor([0.0, 0.5, 1.0])
print('\nTask 3: Call the API torch.bucketize')
print('input: ', input)
print('boundaries: ', boundaries)
print('torch.bucketize(input, boundaries): ', torch.bucketize(input, boundaries))