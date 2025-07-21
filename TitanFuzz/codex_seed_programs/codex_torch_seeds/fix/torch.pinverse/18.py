'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.randn(3, 3, requires_grad=True)
print(input)
output = torch.pinverse(input)
print(output)