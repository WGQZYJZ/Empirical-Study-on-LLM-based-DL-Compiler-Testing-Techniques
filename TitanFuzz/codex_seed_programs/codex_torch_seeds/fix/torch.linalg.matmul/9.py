'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 4)
other = torch.randn(4, 5)
output = torch.linalg.matmul(input, other)
print(output)
out = torch.randn(3, 5)
torch.linalg.matmul(input, other, out=out)
print(out)