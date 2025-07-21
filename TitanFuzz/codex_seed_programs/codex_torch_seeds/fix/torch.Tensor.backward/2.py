'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
import torch.nn as nn
x = torch.randn(3, requires_grad=True)
y = (x * 2)
while (y.data.norm() < 1000):
    y = (y * 2)
print(y)
gradients = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(gradients)
print(x.grad)