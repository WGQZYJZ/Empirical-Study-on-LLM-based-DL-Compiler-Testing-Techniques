'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
start = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.rand(4, 4)
output = torch.lerp(start, end, weight)
print(output)