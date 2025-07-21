'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import numpy as np
input = torch.tensor([(- 5), (- 2), 0, 1, 3, 4, 5, 6, 8, 9, 10])
boundaries = torch.tensor([0, 5, 10])
output = torch.bucketize(input, boundaries)
print(output)