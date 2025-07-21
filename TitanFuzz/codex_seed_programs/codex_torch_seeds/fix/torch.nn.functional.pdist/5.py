'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
x = torch.rand(10, 3)
torch.nn.functional.pdist(x, p=2)