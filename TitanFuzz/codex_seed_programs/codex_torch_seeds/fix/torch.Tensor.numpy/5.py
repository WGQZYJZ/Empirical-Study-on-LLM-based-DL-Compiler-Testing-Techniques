'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print(_input_tensor)
_numpy_array = _input_tensor.numpy()
print(_numpy_array)
_input_tensor.add_(1)
print(_input_tensor)
print(_numpy_array)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(_input_numpy_array)\n'
import numpy as np
_input_numpy_array = np.random.randn(2, 3)
print(_input_numpy_array)
_tensor_from_numpy = torch.from_numpy(_input_numpy_array)
print(_tensor_from_numpy)
_input_numpy_array += 1
print(_input_numpy_array)
print(_tensor_from_numpy)
_tensor_from_numpy.add_(1)