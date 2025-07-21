'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
input = torch.tensor([(- 1.1), (- 0.5), 0.5, 1.1])
boundaries = torch.tensor([(- 1), 0, 1])
bucket_indices = torch.bucketize(input, boundaries, right=True)
print(bucket_indices)
print(type(bucket_indices))
'\nTask 4: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
(unique_indices, unique_counts) = torch.unique(bucket_indices, return_counts=True)
print(unique_indices)
print(unique_counts)
'\nTask 5: Call the API torch.bincount\ntorch.bincount(input, weights=None, minlength=0)\n'