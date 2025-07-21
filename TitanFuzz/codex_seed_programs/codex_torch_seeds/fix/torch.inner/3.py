'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, requires_grad=True)
other_data = torch.randn(3, requires_grad=True)
output = torch.inner(input_data, other_data)
print(output)