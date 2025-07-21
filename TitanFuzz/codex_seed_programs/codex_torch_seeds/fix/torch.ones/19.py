'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones\ntorch.ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.ones(4, 4)
print(input_data)
'\nTask 4: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.zeros(4, 4)
print(input_data)
'\nTask 5: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.rand(4, 4)
print(input_data)
'\nTask 6: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.randn(4, 4)
print(input_data)