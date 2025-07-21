'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
input = torch.randn(3, 3)
boundaries = torch.tensor([0.5, 1.5])
out = torch.bucketize(input, boundaries)
print(out)
out = torch.bucketize(input, boundaries, right=True)
print(out)
out = torch.bucketize(input, boundaries, out_int32=True)
print(out)