'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
input_data = torch.tensor([1.2, 3.4, 5.6, 7.8, 9.0])
boundaries = torch.tensor([3.0, 6.0, 9.0])
output = torch.bucketize(input_data, boundaries)
print(output)