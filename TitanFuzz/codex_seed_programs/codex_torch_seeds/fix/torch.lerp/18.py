'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
start = torch.rand(3, 3)
end = torch.rand(3, 3)
weight = torch.rand(3, 3)
output = torch.lerp(start, end, weight)
print(output)