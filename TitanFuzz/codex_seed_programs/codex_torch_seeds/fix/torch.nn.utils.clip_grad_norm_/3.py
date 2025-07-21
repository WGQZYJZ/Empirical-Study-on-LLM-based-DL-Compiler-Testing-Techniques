'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('\nTask 2: Generate input data')
input_data = np.random.rand(3, 10)
input_data = Variable(torch.from_numpy(input_data), requires_grad=True)
print('Input data: {}'.format(input_data))
print('\nTask 3: Call the API torch.nn.utils.clip_grad_norm_')
print('torch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)')
norm = nn.utils.clip_grad_norm_(input_data, max_norm=2)
print('norm: {}'.format(norm))