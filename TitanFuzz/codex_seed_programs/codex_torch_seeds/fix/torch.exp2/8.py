'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
data = torch.rand(3, 3)
print(data)
result = torch.exp2(data)
print(result)