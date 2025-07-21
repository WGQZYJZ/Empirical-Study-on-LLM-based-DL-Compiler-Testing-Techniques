'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
output_data = torch.from_numpy(input_data)
print(input_data)
print(output_data)