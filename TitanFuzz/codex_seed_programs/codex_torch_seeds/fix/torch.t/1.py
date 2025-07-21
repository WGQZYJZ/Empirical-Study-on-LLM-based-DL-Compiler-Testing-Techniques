'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.t\ntorch.t(input)\n'
import torch
input = torch.randn(3, 3)
print(input)
output = torch.t(input)
print(output)
print(input.size(), output.size())