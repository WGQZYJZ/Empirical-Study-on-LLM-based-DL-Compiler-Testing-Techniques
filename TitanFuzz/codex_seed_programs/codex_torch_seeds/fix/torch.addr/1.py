'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addr\ntorch.addr(input, vec1, vec2, *, beta=1, alpha=1, out=None)\n'
import torch
import torch
input = torch.randn(4, 4, dtype=torch.float)
vec1 = torch.randn(4, dtype=torch.float)
vec2 = torch.randn(4, dtype=torch.float)
output = torch.addr(input, vec1, vec2)
print(output)