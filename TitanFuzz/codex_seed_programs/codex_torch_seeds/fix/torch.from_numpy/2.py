'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
torch_from_numpy_result = torch.from_numpy(input_data)
print('input_data: {}'.format(input_data))
print('torch_from_numpy_result: {}'.format(torch_from_numpy_result))