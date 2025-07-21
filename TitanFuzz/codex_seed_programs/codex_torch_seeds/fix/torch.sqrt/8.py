'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
input = torch.randn(1, requires_grad=True)
output = torch.sqrt(input)
print(output)
output.backward(retain_graph=True)
print(input.grad)
print((input.grad == (0.5 / output)))