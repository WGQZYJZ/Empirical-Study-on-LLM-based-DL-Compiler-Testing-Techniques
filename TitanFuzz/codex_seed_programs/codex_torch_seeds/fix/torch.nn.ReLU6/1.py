'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
import numpy as np
x = torch.randn(3, 5)
print('Input data: ', x)
relu6 = torch.nn.ReLU6()
y = relu6(x)
print('Output data: ', y)