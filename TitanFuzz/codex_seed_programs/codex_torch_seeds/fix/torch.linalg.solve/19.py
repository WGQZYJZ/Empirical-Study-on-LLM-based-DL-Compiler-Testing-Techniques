'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.solve\ntorch.linalg.solve(A, B, *, out=None)\n'
import torch
from torch import Tensor
from typing import Tuple
A = Tensor([[1.0, 2.0], [3.0, 4.0]])
b = Tensor([[5.0], [6.0]])
x = torch.linalg.solve(A, b)
print(x)