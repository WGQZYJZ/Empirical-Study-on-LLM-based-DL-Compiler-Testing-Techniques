'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('\nPyTorch version:', torch.__version__)
print('\nTask 2: Generate input data')
data = torch.rand(2, 3)
print('\nInput data:', data)
print('\nTask 3: Call the API torch.arctan')
print('\nOutput:', torch.arctan(data))