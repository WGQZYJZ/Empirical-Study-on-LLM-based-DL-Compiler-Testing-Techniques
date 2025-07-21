'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
output = torch.cholesky_inverse(input_data)
print(output)
input_data = torch.rand(3, 3)
output = torch.cholesky_inverse(input_data, upper=True)
print(output)