'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3, requires_grad=True)
output = torch.arctanh(input_data)
print('The output tensor: ', output)
print('The gradients w.r.t the input: ', output.grad_fn)
print('The gradients of output w.r.t input: ', output.grad)