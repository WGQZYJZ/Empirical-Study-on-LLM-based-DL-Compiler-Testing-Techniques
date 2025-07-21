'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
x = np.random.rand(10, 3)
print('x: ', x)
x_tensor = torch.from_numpy(x)
print('x_tensor: ', x_tensor)
x_tensor2 = torch.tensor(x)
print('x_tensor2: ', x_tensor2)
x_tensor3 = torch.as_tensor(x)
print('x_tensor3: ', x_tensor3)
x_tensor4 = torch.from_numpy(x.astype(np.int32))
print('x_tensor4: ', x_tensor4)