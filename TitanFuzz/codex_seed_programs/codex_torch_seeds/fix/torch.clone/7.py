'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
input = torch.randn(2, 3, requires_grad=True)
print(input)
output = torch.clone(input)
print(output)
print(torch.equal(input, output))