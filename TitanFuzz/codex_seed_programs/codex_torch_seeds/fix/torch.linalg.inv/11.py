'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
import numpy as np
A = torch.randn(3, 3)
A.requires_grad_(True)
invA = torch.linalg.inv(A)