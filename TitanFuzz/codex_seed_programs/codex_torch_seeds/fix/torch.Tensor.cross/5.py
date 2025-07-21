'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cross\ntorch.Tensor.cross(_input_tensor, other, dim=-1)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.randn(3, requires_grad=True)
a = torch.Tensor.cross(x, y, dim=0)
print('cross product of x and y: {}'.format(a))
b = torch.Tensor.cross(x, y, dim=1)
print('cross product of x and y: {}'.format(b))