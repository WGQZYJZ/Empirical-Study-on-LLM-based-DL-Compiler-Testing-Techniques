'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
data = torch.randn(3, 4)
print('Input data: ', data)
boundaries = torch.tensor([0.0, 0.5, 1.5])
print('Boundaries: ', boundaries)
out = torch.bucketize(data, boundaries)
print('Output: ', out)
print('Output type: ', out.dtype)