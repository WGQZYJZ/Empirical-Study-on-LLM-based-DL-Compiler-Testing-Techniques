'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
input = torch.rand(4, 4)
tensor1 = torch.rand(4, 4)
tensor2 = torch.rand(4, 4)
print(input)
print(tensor1)
print(tensor2)
print(torch.addcdiv(input, tensor1, tensor2))
print(torch.addcdiv(input, tensor1, tensor2, value=2))
print(torch.addcdiv(input, tensor1, tensor2, value=2, out=torch.empty(4, 4)))
print(torch.addcdiv(input, tensor1, tensor2, value=2, out=torch.empty(4, 4).fill_(10)))
print(torch.addcdiv(input, tensor1, tensor2, value=2, out=torch.empty(4, 4).fill_(10)).size())