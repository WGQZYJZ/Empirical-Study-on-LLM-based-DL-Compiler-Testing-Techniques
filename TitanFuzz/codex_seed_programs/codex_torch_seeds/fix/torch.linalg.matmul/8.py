'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, requires_grad=True)
other = torch.randn(3, 3, requires_grad=True)
bias = torch.randn(2, 3, requires_grad=True)
output = torch.linalg.matmul(input, other)
output = (output + bias)
output.backward(torch.ones(output.shape))
print(input.grad)
print(other.grad)
print(bias.grad)