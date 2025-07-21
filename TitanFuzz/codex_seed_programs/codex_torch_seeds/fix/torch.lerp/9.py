'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
input = torch.rand(4, 3, dtype=torch.float)
end = torch.rand(4, 3, dtype=torch.float)
weight = torch.rand(4, 3, dtype=torch.float)
out = torch.lerp(input, end, weight)
print('input: ', input)
print('end: ', end)
print('weight: ', weight)
print('out: ', out)