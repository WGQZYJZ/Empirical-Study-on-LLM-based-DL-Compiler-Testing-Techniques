'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.randn(5, 5)
pinv_input = torch.pinverse(input)
print('Input:', input)
print('Pseudo-Inverse of input:', pinv_input)