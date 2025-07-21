'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.det\ntorch.linalg.det(A, *, out=None)\n'
import torch
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
torch.linalg.det(A)