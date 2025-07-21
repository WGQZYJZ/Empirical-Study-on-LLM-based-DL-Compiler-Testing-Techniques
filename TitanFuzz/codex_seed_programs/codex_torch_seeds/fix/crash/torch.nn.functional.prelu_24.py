'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
weight = torch.randn(1, 3, requires_grad=True)
print(input)
print(weight)
output = F.prelu(input, weight)
print(output)
output.backward(torch.randn(2, 3))
print(weight.grad)