'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
import torch.nn.functional as F
import torch
data = torch.randn(3, 4)
print(data)
output = F.pdist(data, p=2)
print(output)