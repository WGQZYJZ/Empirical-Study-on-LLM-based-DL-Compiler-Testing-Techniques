'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
import numpy as np
data = np.random.rand(5, 5)
data = torch.tensor(data)
output = torch.Tensor.expm1(data)
print('Input data:')
print(data)
print('Output data:')
print(output)