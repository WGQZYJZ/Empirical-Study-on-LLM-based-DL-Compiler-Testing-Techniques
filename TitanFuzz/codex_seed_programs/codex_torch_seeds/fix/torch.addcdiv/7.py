'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.randn(4, 4)
print(torch.addcdiv(a, b, c))
print(torch.addcdiv(a, b, c, value=1))