'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
mat2 = torch.randn(2, 4, 5)
output = torch.bmm(input, mat2)
print('input: ', input)
print('mat2: ', mat2)
print('output: ', output)