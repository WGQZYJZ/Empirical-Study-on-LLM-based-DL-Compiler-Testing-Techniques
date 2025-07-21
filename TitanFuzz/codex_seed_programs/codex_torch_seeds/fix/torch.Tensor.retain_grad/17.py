'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
import numpy as np
a = torch.randn(3, requires_grad=True)
b = (a * 2)
while (b.data.norm() < 1000):
    b = (b * 2)
b.retain_grad()
if (b.grad is None):
    print('b.grad is None')
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
b.backward(v)
print(a.grad)