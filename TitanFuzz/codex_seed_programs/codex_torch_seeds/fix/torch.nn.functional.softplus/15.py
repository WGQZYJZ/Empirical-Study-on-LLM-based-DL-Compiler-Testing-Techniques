'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
import numpy as np
input = torch.randn(4, 4, requires_grad=True)
print('input: ', input)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)
print('output: ', output)
output.backward(torch.ones(4, 4))
print('grad: ', input.grad)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)
print('output: ', output)
output.backward(torch.ones(4, 4))
print('grad: ', input.grad)