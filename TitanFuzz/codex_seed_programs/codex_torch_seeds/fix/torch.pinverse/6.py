'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).float()
print('A = ', A)
A_inv = torch.pinverse(A)
print('A_inv = ', A_inv)
print('A * A_inv = ', torch.mm(A, A_inv))