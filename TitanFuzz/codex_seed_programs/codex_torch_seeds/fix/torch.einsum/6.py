'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
input1 = torch.randn(2, 3)
print('input1: ', input1)
input2 = torch.randn(3, 2)
print('input2: ', input2)
output = torch.einsum('ij,jk->ik', input1, input2)
print('output: ', output)