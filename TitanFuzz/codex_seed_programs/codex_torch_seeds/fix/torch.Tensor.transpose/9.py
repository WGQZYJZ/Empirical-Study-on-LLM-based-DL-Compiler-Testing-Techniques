'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
a_tensor = torch.Tensor(a)
print(a_tensor.transpose(0, 1))
print(a_tensor.transpose(1, 0))