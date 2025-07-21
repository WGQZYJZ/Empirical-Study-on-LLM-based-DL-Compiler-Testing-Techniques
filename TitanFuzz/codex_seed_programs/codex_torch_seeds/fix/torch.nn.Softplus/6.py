'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import numpy as np
import torch
x = torch.randn(1, 1, requires_grad=True)
y = torch.nn.Softplus()(x)
print(y)
y.backward()
print(x.grad)