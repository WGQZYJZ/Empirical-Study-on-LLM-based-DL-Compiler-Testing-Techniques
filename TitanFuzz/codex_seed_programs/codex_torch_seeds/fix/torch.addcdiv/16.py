'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
input = torch.randn(4, 4)
tensor1 = torch.randn(4, 4)
tensor2 = torch.randn(4, 4)
output = torch.addcdiv(input, tensor1, tensor2, value=1)
print('input: ', input)
print('tensor1: ', tensor1)
print('tensor2: ', tensor2)
print('output: ', output)