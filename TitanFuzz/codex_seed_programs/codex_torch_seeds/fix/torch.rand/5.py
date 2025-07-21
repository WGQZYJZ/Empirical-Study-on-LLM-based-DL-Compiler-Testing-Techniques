'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
output_data = torch.rand(2, 3)
print(output_data)
'\nTask 4: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.randn(2, 3)
print(input_data)
'\nTask 5: Call the API torch.randint\ntorch.randint(low, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
input_data = torch.randint(5, 10, (2, 3))
print(input_data)