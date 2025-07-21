'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
import torch
input = torch.rand(10, 3, 4)
mat2 = torch.rand(10, 4, 5)
output = torch.bmm(input, mat2)
print(output.size())