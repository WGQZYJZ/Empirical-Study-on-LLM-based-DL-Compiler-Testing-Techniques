'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input = torch.randn(3, 1, 3)
print(input)
print(torch.unbind(input, dim=0))
print(torch.unbind(input, dim=1))
print(torch.unbind(input, dim=2))
print(torch.stack(torch.unbind(input, dim=0), dim=0))
print(torch.stack(torch.unbind(input, dim=1), dim=1))
print(torch.stack(torch.unbind(input, dim=2), dim=2))