'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
input = torch.arange(0, 10, 0.1)
boundaries = torch.tensor([0, 5, 9])
out = torch.bucketize(input, boundaries, out_int32=True, right=False)
print(out)
out = torch.bucketize(input, boundaries, out_int32=True, right=True)
print(out)