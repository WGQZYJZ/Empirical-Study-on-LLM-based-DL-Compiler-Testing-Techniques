'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
import numpy as np
x = torch.rand(5, 5)
y = torch.rand(5, 5)
z = torch.rand(5, 5)
print(torch.addcdiv(x, y, z))