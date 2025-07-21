'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input = torch.randn(1, 3)
print(input)
result = torch.aminmax(input, dim=1)
print(result)