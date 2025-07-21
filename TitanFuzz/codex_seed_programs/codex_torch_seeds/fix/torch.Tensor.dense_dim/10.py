'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dense_dim\ntorch.Tensor.dense_dim(_input_tensor)\n'
import torch
import numpy as np
input_tensor = np.random.rand(3, 3, 3)
print(input_tensor)
input_tensor = torch.tensor(input_tensor)
print(input_tensor)
print(input_tensor.dense_dim())