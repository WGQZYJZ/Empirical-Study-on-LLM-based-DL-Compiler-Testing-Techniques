'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
A = torch.tensor([[1, 2], [3, 4]]).float()
B = torch.tensor([[1, 2], [3, 4]]).float()
torch.linalg.lstsq(A, B, rcond=None, driver=None)