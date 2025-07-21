'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.randn(4, 4)
output = torch.lerp(input, end, weight)
print(output)