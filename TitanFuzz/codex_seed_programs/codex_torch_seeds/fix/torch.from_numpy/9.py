'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
print('\nnumpy array: \n', np_data)
print('\ntorch tensor: \n', torch_data)
np_data = torch_data.numpy()
print('\nnumpy array: \n', np_data)
data = [(- 1), (- 2), 1, 2]
tensor = torch.FloatTensor(data)
print('\nabs: \n', torch.abs(tensor))
print('\nsin: \n', torch.sin(tensor))
print('\nmean: \n', torch.mean(tensor))
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor