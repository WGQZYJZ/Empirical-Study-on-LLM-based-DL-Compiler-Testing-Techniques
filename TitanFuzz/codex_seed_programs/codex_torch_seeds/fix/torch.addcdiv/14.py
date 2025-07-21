'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
import torch
tensor1 = torch.randn(2, 2)
tensor2 = torch.randn(2, 2)
tensor3 = torch.randn(2, 2)
print('tensor1: ', tensor1)
print('tensor2: ', tensor2)
print('tensor3: ', tensor3)
tensor4 = torch.addcdiv(tensor1, tensor2, tensor3, value=1)
print('tensor4: ', tensor4)