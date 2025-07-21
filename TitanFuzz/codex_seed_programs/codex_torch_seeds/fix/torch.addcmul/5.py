'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
import numpy as np
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.randn(4, 4)
torch.addcmul(x, y, z)
print(x)