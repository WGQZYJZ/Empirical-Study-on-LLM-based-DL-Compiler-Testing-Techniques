'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
input1 = torch.randn(2, 3)
input2 = torch.randn(4, 5)
print(input1)
print(input2)
print(torch.kron(input1, input2))