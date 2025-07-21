'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
print('input data: \n', input_data)
print('input data type: ', type(input_data))
input_tensor = torch.from_numpy(input_data)
print('input tensor: \n', input_tensor)
print('input tensor type: ', type(input_tensor))
input_tensor = input_tensor.double()
print('input tensor: \n', input_tensor)
print('input tensor type: ', type(input_tensor))