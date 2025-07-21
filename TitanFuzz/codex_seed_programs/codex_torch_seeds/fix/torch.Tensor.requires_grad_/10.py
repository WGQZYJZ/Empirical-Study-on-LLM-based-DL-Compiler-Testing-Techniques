'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
x = torch.tensor(2.0, requires_grad=True)
y = (((((9 * (x ** 4)) + (2 * (x ** 3))) + (3 * (x ** 2))) + (6 * x)) + 1)
print('The result of y: ', y)
y.requires_grad_(True)
print('The result of y.requires_grad: ', y.requires_grad)
print('The result of x.requires_grad: ', x.requires_grad)
y.backward()
print('The dervative at x=2: ', x.grad)