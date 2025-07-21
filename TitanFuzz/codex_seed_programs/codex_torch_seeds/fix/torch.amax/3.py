'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
print(torch.amax(input, dim=0))
print(torch.amax(input, dim=1))
print(torch.amax(input, dim=2))
print(torch.amax(input, dim=0, keepdim=True))
print(torch.amax(input, dim=1, keepdim=True))
print(torch.amax(input, dim=2, keepdim=True))
print(torch.amax(input, dim=0, out=torch.empty(3, 5)))
print(torch.amax(input, dim=1, out=torch.empty(2, 5)))
print(torch.amax(input, dim=2, out=torch.empty(2, 3)))