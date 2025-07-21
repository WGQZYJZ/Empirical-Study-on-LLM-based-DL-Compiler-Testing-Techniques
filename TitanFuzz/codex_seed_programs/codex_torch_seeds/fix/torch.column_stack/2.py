'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.randn(2, 3)
stack = torch.column_stack((x, y, z))
print('stack: ', stack)
'\nOutput:\nstack:  tensor([[-0.5662,  0.0365, -0.5244, -0.1654, -0.5673, -0.5200],\n        [-0.6317, -0.9808,  0.5147,  0.1642,  0.0267,  0.9359]])\n'