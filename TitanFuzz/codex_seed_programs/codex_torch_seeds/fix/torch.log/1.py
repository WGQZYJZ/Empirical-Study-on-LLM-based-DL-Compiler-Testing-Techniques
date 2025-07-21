'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
input = torch.randn(1, requires_grad=True)
output = torch.log(input)
print(input, output)
output.backward(retain_graph=True)
print(input.grad)