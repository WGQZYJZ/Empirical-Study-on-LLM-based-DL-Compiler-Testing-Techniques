'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([[3, 1], [1, 2]])
print(input_data)
print(torch.from_numpy(input_data))
print(torch.tensor(input_data))
print(torch.as_tensor(input_data))
print(torch.from_numpy(input_data).type())