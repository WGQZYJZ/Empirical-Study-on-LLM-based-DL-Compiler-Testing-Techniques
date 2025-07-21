'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
batch = 2
input = torch.randn(batch, 3, 4)
mat2 = torch.randn(batch, 4, 5)
output = torch.bmm(input, mat2)
print(output)
output = torch.bmm(input, mat2, out=torch.zeros(batch, 3, 5))
print(output)