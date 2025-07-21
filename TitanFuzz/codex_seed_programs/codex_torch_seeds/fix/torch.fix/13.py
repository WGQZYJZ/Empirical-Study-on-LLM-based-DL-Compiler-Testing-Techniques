'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
import torch
input = torch.randn(10)
output = torch.fix(input)
print(input)
print(output)
print(torch.equal(input, output))