'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.randn(2, 3, requires_grad=True)
print('Input matrix: ', input)
pinv_input = torch.pinverse(input)
print('Pseudo inverse of input matrix: ', pinv_input)
pinv_input = torch.pinverse(input, rcond=0.001)
print('Pseudo inverse of input matrix with rcond = 1e-3: ', pinv_input)