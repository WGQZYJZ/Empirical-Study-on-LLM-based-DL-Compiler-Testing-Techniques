'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
import numpy as np
x = torch.arange(1, 10, dtype=torch.float32).view(3, 3)
print('x: ', x)
y = torch.fliplr(x)
print('y: ', y)