'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
input = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.addcmul(input, tensor1, tensor2)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
input = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.addcdiv(input, tensor1, tensor2)