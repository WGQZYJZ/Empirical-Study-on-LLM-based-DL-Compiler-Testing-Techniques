'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv_ex\ntorch.linalg.inv_ex(A, *, check_errors=False, out=None)\n'
import torch
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float64)
print('A: ', A)
inv_A = torch.linalg.inv_ex(A)
print('inv_A: ', inv_A)