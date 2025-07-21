'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
x = torch.randn(2, 2, requires_grad=True)
y = (x ** 2)
y.retain_grad()
z = y.sum()
z.backward()
print(x.grad)
print(y.grad)
print(z.grad)