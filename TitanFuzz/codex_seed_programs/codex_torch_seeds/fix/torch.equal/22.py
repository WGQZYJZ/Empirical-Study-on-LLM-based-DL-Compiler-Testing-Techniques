'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
input = torch.rand(2, 3)
other = torch.rand(2, 3)
output = torch.equal(input, other)
print(output)