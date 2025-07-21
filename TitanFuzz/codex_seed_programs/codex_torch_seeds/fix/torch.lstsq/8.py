'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
b = torch.tensor([[1.0], [2.0], [3.0]])
(x, _) = torch.lstsq(b, A)
print(x)
print((A @ x))