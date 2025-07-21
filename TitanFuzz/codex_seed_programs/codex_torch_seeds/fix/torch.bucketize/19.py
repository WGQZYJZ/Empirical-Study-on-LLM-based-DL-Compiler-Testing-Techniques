'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
input = torch.tensor([(- 1.0), 0.0, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
boundaries = torch.tensor([1.0, 4.0, 6.0])
output = torch.bucketize(input, boundaries, right=True)
print(output)
output = torch.bucketize(input, boundaries, right=False)
print(output)