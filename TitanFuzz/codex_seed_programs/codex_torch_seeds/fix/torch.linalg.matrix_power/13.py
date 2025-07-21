'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
print('A =', A)
A2 = torch.linalg.matrix_power(A, 2)
print('A^2 =', A2)
A3 = torch.linalg.matrix_power(A, 3)
print('A^3 =', A3)
A4 = torch.linalg.matrix_power(A, 4)
print('A^4 =', A4)
A5 = torch.linalg.matrix_power(A, 5)
print('A^5 =', A5)