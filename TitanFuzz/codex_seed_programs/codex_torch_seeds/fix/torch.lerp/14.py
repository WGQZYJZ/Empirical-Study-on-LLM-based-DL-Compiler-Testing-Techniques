'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
input = torch.randn(5, 3)
end = torch.randn(5, 3)
weight = torch.rand(5, 3)
torch.lerp(input, end, weight)