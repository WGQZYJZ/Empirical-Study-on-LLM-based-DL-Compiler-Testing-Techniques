'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
A = torch.randn(3, 3)
B = torch.randn(3, 2)
output = torch.linalg.lstsq(A, B)
print('The output of torch.linalg.lstsq: ', output)