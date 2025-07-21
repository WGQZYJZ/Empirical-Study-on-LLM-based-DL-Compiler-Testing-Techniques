'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.log_softmax\ntorch.sparse.log_softmax(input, dim, dtype=None)\n'
import torch
import numpy as np
input = torch.randn(3, 3)
input = input.to_sparse()
print(input)
print(torch.sparse.log_softmax(input, dim=1))