'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
a = torch.rand(4, 4)
b = torch.rand(4, 4)
c = torch.rand(4, 4)
print(torch.addcmul(a, b, c))