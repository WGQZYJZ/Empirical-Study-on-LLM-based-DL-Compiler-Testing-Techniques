'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
torch.Tensor.requires_grad_(x, requires_grad=True)
print('x: {}'.format(x))
print('x.requires_grad: {}'.format(x.requires_grad))