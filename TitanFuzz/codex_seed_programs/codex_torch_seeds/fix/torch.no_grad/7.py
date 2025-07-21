'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
input_data = torch.randn(3, requires_grad=True)
print('input_data: ', input_data)
with torch.no_grad():
    output = (input_data * 2)
print('output: ', output)
print('output.requires_grad: ', output.requires_grad)
print('output.grad_fn: ', output.grad_fn)