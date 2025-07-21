'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.randn(2, 3, requires_grad=True)
print('Input: ', input)
output = torch.pinverse(input)
print('Output: ', output)