'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
data = np.random.rand(2, 3)
data = torch.from_numpy(data)
print('data: {}'.format(data))
print('Task 3: Call the API torch.nn.utils.clip_grad_value_')
clip_value = 0.5
torch.nn.utils.clip_grad_value_(data, clip_value)
print('data: {}'.format(data))