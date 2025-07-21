'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
A = torch.randn(3, 3, requires_grad=True)
pinv_A = torch.pinverse(A)
print(pinv_A)