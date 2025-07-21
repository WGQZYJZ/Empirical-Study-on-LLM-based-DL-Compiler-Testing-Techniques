'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4, requires_grad=True)
end = torch.randn(3, 4, requires_grad=True)
weight = torch.randn(3, 4, requires_grad=True)
output = torch.lerp(input, end, weight)
print(output)