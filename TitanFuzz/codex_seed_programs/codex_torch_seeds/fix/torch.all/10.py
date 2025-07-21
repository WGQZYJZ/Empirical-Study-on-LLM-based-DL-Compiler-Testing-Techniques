'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int32)
print(input)
output = torch.all(input, dim=0)
print(output)