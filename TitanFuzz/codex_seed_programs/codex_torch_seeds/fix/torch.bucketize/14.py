'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
data = torch.randn(3, 4)
boundaries = torch.tensor([0.5, 1.5])
torch.bucketize(input=data, boundaries=boundaries)
print(torch.bucketize(input=data, boundaries=boundaries))
print(torch.bucketize(input=data, boundaries=boundaries, right=True))