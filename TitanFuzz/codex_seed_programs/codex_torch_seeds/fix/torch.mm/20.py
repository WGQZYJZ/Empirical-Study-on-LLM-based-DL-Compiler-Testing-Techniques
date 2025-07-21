'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 3)
mat2 = torch.randn(3, 5)
output = torch.mm(input, mat2)
print(output)
print(output.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, out=None)\n'
import torch
import torch
input1 = torch.randn(10, 3, 4)
input2 = torch.randn(10, 4, 5)
output = torch.bmm(input1, input2)
print(output.size())