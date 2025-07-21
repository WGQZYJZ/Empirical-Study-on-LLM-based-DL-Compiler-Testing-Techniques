'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
input = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])
boundaries = torch.tensor([2, 4, 6, 8])
result = torch.bucketize(input, boundaries, out_int32=True, right=False)
print(result)
'\nTask 4: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
input = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])
boundaries = torch.tensor([2, 4, 6, 8])
result = torch.bucketize(input, boundaries, out_int32=True, right=True)