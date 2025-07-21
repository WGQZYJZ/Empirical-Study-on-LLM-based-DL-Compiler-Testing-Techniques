'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
print(torch.aminmax(input))
print(torch.aminmax(input, dim=0))
print(torch.aminmax(input, dim=1))
print(torch.aminmax(input, dim=2))
print(torch.aminmax(input, dim=1, keepdim=True))
print(torch.aminmax(input, dim=2, keepdim=True))