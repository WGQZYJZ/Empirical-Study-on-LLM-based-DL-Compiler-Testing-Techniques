'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print(input)
output = torch.eig(input)
print(output)
output = torch.eig(input, True)
print(output)