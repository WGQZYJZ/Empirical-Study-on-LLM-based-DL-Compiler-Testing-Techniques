'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cov\ntorch.cov(input, *, correction=1, fweights=None, aweights=None)\n'
import torch
import torch
input = torch.randint(0, 9, (3, 3))
print(input)
torch.cov(input, correction=1)
torch.cov(input, correction=0)