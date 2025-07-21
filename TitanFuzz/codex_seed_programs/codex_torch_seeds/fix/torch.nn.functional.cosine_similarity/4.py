'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_similarity\ntorch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-8)\n'
import torch
import numpy as np
x1 = torch.randn(1, 3)
x2 = torch.randn(1, 3)
y = torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)
print('x1: ', x1)
print('x2: ', x2)
print('y: ', y)