'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
input = torch.rand(4, 4)
boundaries = torch.tensor([0.2, 0.6])
bucketized_tensor = torch.bucketize(input, boundaries)
print(bucketized_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bincount\ntorch.bincount(input, *, weights=None, minlength=0)\n'
import torch
import torch
input = torch.tensor([1, 2, 4, 4, 2, 1])
bincount = torch.bincount(input)
print(bincount)