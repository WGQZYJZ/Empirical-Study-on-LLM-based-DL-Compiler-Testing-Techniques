'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
import numpy as np
x = torch.arange(12).view(3, 4).float()
print('x =', x)
y = torch.fliplr(x)
print('y =', y)
x_numpy = np.arange(12).reshape(3, 4)
print('x_numpy =', x_numpy)
y_numpy = np.fliplr(x_numpy)
print('y_numpy =', y_numpy)