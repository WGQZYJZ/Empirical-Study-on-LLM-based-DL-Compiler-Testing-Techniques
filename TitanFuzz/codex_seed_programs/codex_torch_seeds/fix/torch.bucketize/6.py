'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
input = torch.randn(5)
boundaries = torch.tensor([0.0, 1.0])
torch.bucketize(input, boundaries)