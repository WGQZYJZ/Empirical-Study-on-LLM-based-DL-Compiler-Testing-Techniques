'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_input_tensor = torch.from_numpy(A)
print('The input tensor is: \n{}'.format(_input_tensor))
print('The output tensor is: \n{}'.format(_input_tensor.matrix_power(2)))