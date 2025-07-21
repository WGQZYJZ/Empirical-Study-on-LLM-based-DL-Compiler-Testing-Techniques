'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(1, 2, 3)
print(input_data)
'\nTask 4: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.randn(1, 2, 3)
print(input_data)
'\nTask 5: Call the API torch.randperm\ntorch.randperm(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.randperm(4)
print(input_data)
'\nTask 6: Call the API torch.arange\ntorch.arange(*start, *stop, *step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.arange(0, 10, 2)