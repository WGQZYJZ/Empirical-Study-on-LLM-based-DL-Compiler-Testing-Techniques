'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.randn(3, 5, dtype=torch.float, requires_grad=True)
pinv_input = torch.pinverse(input)
print('The input data is: \n', input)
print('The pinv of input data is: \n', pinv_input)