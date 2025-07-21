'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
input = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
print(torch.special.gammaln(input))