'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
input = torch.randn(3, requires_grad=True)
print(input)
output = torch.negative(input)
print(output)
output.backward(torch.ones(input.size()))
print(input.grad)