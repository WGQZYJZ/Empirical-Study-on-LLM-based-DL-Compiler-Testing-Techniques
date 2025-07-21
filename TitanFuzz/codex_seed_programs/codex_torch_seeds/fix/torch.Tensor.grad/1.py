'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.grad\ntorch.Tensor.grad(_input_tensor, )\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
grad_tensor = torch.Tensor.grad(input_tensor, input_tensor)
print('input_tensor: ', input_tensor)
print('grad_tensor: ', grad_tensor)
'\noutput:\ninput_tensor:  tensor([[1., 2., 3.],\n        [4., 5., 6.]], requires_grad=True)\ngrad_tensor:  tensor([[1., 1., 1.],\n        [1., 1., 1.]])\n'