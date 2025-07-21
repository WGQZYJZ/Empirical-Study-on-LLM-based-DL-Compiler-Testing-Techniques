'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.equal(input, other)
torch.equal(input, input)
torch.equal(input, other)