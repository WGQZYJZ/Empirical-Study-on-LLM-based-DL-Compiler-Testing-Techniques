'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.register_hook\ntorch.Tensor.register_hook(_input_tensor, hook)\n'
import torch
x = torch.randn(1)
x.requires_grad_(True)
print('x: ', x)
x.register_hook(print)
y = (x ** 2)
print('y: ', y)
z = y.mean()
print('z: ', z)
z.backward()
print('x.grad: ', x.grad)