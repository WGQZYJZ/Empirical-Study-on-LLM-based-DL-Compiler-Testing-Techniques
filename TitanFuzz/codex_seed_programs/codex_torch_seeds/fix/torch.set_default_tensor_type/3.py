'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
import numpy as np
input_data = np.array([[3, 1], [1, 1]])
input_data = torch.Tensor(input_data)
torch.set_default_tensor_type(torch.DoubleTensor)
print('Input data: ', input_data)
print('Data type of input data: ', input_data.dtype)
print('Data type of torch.Tensor: ', torch.Tensor.dtype)
print('Data type of torch.DoubleTensor: ', torch.DoubleTensor.dtype)