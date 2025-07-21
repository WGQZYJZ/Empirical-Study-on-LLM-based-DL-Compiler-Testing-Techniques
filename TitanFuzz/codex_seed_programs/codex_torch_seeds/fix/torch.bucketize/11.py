'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
input = torch.randn(3, 4)
boundaries = torch.tensor([0.5, 1.5])
out = torch.bucketize(input, boundaries)
print(out)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(tensor, chunks, dim=0)\n'
import torch
input = torch.randn(3, 4)
chunks = 2
out = torch.chunk(input, chunks, dim=0)
print(out)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min, max, out=None)\n'
import torch