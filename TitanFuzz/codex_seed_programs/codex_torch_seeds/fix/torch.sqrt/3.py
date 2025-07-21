'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
input = torch.randn(1, requires_grad=True)
output = torch.sqrt(input)
print(output)
print(output.grad_fn)
print(output.grad)
output.backward()
print(output.grad)
print(input.grad)