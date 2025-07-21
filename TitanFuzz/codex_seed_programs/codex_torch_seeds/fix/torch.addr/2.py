'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addr\ntorch.addr(input, vec1, vec2, *, beta=1, alpha=1, out=None)\n'
import torch
input = torch.randn(3, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
output = torch.addr(input, vec1, vec2)
print('Output is: ', output)