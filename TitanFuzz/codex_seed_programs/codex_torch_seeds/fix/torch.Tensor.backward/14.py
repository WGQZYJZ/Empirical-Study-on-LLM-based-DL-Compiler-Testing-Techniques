'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
x = torch.tensor([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]])
x.backward()
print('x.grad: ', x.grad)
print('x.grad_fn: ', x.grad_fn)