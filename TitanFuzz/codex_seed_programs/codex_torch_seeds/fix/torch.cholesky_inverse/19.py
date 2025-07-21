'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
output = torch.cholesky_inverse(input)
print(output)
output2 = torch.cholesky_inverse(input, upper=True)
print(output2)