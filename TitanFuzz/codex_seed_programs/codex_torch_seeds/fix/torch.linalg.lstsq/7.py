'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[1.0], [2.0]])
x = torch.linalg.lstsq(A, b)
print(x)