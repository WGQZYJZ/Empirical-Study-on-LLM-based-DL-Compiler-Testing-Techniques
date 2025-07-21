'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bucketize\ntorch.bucketize(input, boundaries, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
input_data = torch.tensor([(- 5), (- 2), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
bucket_boundaries = torch.tensor([0, 4, 8])
result = torch.bucketize(input_data, bucket_boundaries)
print(result)