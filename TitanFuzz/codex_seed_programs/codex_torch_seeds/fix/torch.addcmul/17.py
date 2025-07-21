'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
t1 = torch.rand(3, 3)
t2 = torch.rand(3, 3)
t3 = torch.rand(3, 3)
print(t1)
print(t2)
print(t3)
torch.addcmul(t1, t2, t3)
print(t1)