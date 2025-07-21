'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(1, 1, 32, 32)
print(input_data.size())
print(torch.randn(1, 1, 32, 32).size())
print(torch.randn(1, 1, 32, 32))
print(torch.randn(1, 1, 32, 32).requires_grad)
print(torch.randn(1, 1, 32, 32, requires_grad=True).requires_grad)
print(torch.randn(1, 1, 32, 32, requires_grad=True))
print(torch.randn(1, 1, 32, 32, requires_grad=True).grad)
print(torch.randn(1, 1, 32, 32, requires_grad=True).grad_fn)