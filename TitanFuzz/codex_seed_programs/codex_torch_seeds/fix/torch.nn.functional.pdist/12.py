'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
input = torch.randn(3, 4)
print(input)
dist = torch.nn.functional.pdist(input, p=2)
print(dist)
dist = torch.nn.functional.pdist(input, p=1)
print(dist)
dist = torch.nn.functional.pdist(input, p=3)
print(dist)
dist = torch.nn.functional.pdist(input, p=4)
print(dist)