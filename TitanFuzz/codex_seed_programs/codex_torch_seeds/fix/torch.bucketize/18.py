'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
input = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
boundaries = torch.tensor([0.0, 1.0, 2.0])
output = torch.bucketize(input, boundaries)
print(output)